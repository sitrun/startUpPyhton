CREATE TABLE
  `breezes` (
    `id` integer not null primary key autoincrement,
    `created_at` datetime not null default CURRENT_TIMESTAMP,
    `breeze_text` TEXT NULL,
    `active` TINYINT null default 1
  );

CREATE TABLE
  `categories` (
    `id` integer not null primary key autoincrement,
    `created_at` datetime not null default CURRENT_TIMESTAMP,
    `cat_name` varchar(255) null,
    `short_name` varchar(255) null,
    `active` TINYINT null default 1
);

CREATE TABLE
  `breezes_category_search` (
    `id` integer not null primary key autoincrement,
    `created_at` datetime not null default CURRENT_TIMESTAMP,
    `id1` INT NULL,
    `id2` INT NULL
  );


insert into breezes (breeze_text, active)
values
    ('Что еще сегодня возможно?', 1),
    ('Какие новые вкусы я сегодня могу ощутить и попробовать?', 1),
    ('У меня все получается по работе, все задачи решаются с легкостью и великолепием, как у талантливого композитора', 1),
    ('Что нужно, чтобы получать больше потоков денег?', 1);

insert into categories (cat_name, short_name, active)
values
    ('Вопросы', 'question', 1),
    ('Аффирмации', 'amalgam', 1);

insert into breezes_category_search (id1, id2)
values
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 1);
