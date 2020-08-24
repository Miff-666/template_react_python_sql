-- FUNCTION: public.auth(text, integer, text)

-- DROP FUNCTION public.auth(text, integer, text);

CREATE OR REPLACE FUNCTION public.auth(
	token_arg text,
	app_id_arg integer,
	timezone_arg text)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
AS $BODY$DECLARE
_is_integration bool;
_timezone text;

BEGIN
	SELECT INTO _is_integration, _timezone
		is_integration, timezone
		FROM users WHERE app_id = app_id_arg
		LIMIT 1;
		
	IF _is_integration IS null THEN
		INSERT INTO users (app_id, token_api, timezone) VALUES (app_id_arg, token_arg, timezone_arg);
		/*log*/
		RETURN '{"is_integration": false, "timezone": null}'::json;
	ELSE
		UPDATE users SET token_api = token_arg, timezone = timezone_arg WHERE app_id = app_id_arg;
	END IF;
	/*log*/
	RETURN '{"is_integration": ' || _is_integration || '}';
END$BODY$;

ALTER FUNCTION public.auth(text, integer, text)
    OWNER TO postgres;


-- FUNCTION: public.get_info(integer)

-- DROP FUNCTION public.get_info(integer);

CREATE OR REPLACE FUNCTION public.get_info(
	app_id_arg integer)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
AS $BODY$DECLARE
_is_integration bool;
_token text;
_timezone text;

BEGIN
	SELECT INTO _is_integration, _token, _timezone
		is_integration, token_api, timezone
		FROM users WHERE app_id = app_id_arg
		LIMIT 1;
	RETURN '{"is_integration": ' || _is_integration || 
		', "timezone": "' || _timezone || 
		'", "token": "' || _token || '"}';
END$BODY$;

ALTER FUNCTION public.get_info(integer)
    OWNER TO postgres;



-- FUNCTION: public.logs(bigint, text, text, text, text)

-- DROP FUNCTION public.logs(bigint, text, text, text, text);

CREATE OR REPLACE FUNCTION public.logs(
	app_id_arg bigint,
	webhook_jsn_arg text,
	dataapi_request_arg text,
	dataapi_response_arg text,
	status_arg text)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
AS $BODY$BEGIN
	INSERT INTO logs (app_id, webhook_jsn, dataapi_request, dataapi_response, status)
		VALUES (app_id_arg, webhook_jsn_arg, dataapi_request_arg, dataapi_response_arg, status_arg);
	return '{"status": "ok"}';
END$BODY$;

ALTER FUNCTION public.logs(bigint, text, text, text, text)
    OWNER TO postgres;



-- FUNCTION: public.update_setting(boolean, integer)

-- DROP FUNCTION public.update_setting(boolean, integer);

CREATE OR REPLACE FUNCTION public.update_setting(
	is_integration_arg boolean,
	app_id_arg integer)
    RETURNS json
    LANGUAGE 'plpgsql'

    COST 100
    VOLATILE 
AS $BODY$BEGIN
	UPDATE users SET 
		is_integration = is_integration_arg
		WHERE app_id = app_id_arg;
	return '{"success": true}';
END$BODY$;

ALTER FUNCTION public.update_setting(boolean, integer)
    OWNER TO postgres;
