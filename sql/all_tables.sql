-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app_id integer NOT NULL,
    token_api text COLLATE pg_catalog."default" NOT NULL,
    is_integration boolean NOT NULL DEFAULT false,
    date timestamp with time zone NOT NULL DEFAULT (now())::timestamp without time zone,
    timezone text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;

GRANT ALL ON TABLE public.users TO postgres;

GRANT ALL ON TABLE public.users TO template;

-- Table: public.logs

-- DROP TABLE public.logs;

CREATE TABLE public.logs
(
    id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app_id bigint NOT NULL,
    data timestamp with time zone NOT NULL DEFAULT (now())::timestamp without time zone,
    webhook_jsn text COLLATE pg_catalog."default",
    dataapi_request text COLLATE pg_catalog."default",
    dataapi_response text COLLATE pg_catalog."default",
    status text COLLATE pg_catalog."default",
    CONSTRAINT log_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.logs
    OWNER to postgres;

GRANT ALL ON TABLE public.logs TO postgres;

GRANT ALL ON TABLE public.logs TO template;