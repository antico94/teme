DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS questions;

CREATE TABLE users
(

    email    CHARACTER VARYING(255),
    password CHARACTER VARYING(1000)
);


INSERT INTO users
VALUES ('john@doe.com', '$2b$12$/TYFvXOy9wDQUOn5SKgTzedwiqB6cm.UIfPewBnz0kUQeK9Eu4mSC');

CREATE TABLE questions
(
    id  serial NOT NULL,
    title  CHARACTER VARYING(1000),
    a      CHARACTER VARYING(1000),
    b      CHARACTER VARYING(1000),
    c      CHARACTER VARYING(1000),
    d      CHARACTER VARYING(1000),
    answer VARCHAR(1)
);

INSERT INTO questions (title, a, b, c, d, answer)
VALUES ('I ______ bus on Mondays.',
        'a. '' m going to work with',
        'b. ''m going to work by',
        'c. go to work with',
        'd. go to work by',
        'd'),

       ('Sorry, but this chair is ______.',
        'a. me',
        'b. mine',
        'c. my',
        'd. our',
        'b'),
       ('A: ''How old ______?''   B: ''I ______ .''',
        'a. are you / am 20 years old.',
        'b. have you / have 20 years old.',
        'c. are you / am 20 years.',
        'd. do you have / have 20 years.',
        'a'),
       ('I ______ to the cinema.',
        'a. usually don''t go',
        'b. don''t usually go',
        'c. don''t go usually',
        'd. do not go usually',
        'b'),
       ('Where ______ ?',
        'a. your sister works',
        'b. your sister work',
        'c. does your sister work',
        'd. do your sister work',
        'c');


