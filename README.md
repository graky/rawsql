Скрипт создания таблицы


CREATE TABLE public.lesson_lesson
(
    id uuid NOT NULL DEFAULT uuid_generate_v4() PRIMARY KEY,
    title character(128)  NOT NULL,
    subtitle character(128) NOT NULL,
    date_created timestamp with time zone NOT NULL DEFAULT CURRENT_DATE
)
