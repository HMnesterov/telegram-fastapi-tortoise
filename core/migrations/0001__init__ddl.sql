CREATE TABLE IF NOT EXISTS TGUser
(
    id            BIGINT PRIMARY KEY NOT NULL ,
    hash          VARCHAR(999) NOT NULL,
    first_name    VARCHAR(255) NULL,
    username      VARCHAR(255) NULL,
    language_code VARCHAR(255) NULL,
    is_bot        BOOLEAN      NOT NULL

);

CREATE TABLE IF NOT EXISTS TGChat
(
    id    BIGINT PRIMARY KEY NOT NULL ,
    hash  VARCHAR(999) NOT NULL,
    full_name VARCHAR(255) NOT NULL ,
    type  VARCHAR(255) NULL

);

CREATE TABLE IF NOT EXISTS TGMessage
(
    true_id  UUID PRIMARY KEY NOT NULL ,
    id BIGINT NOT NULL,
    author_id  BIGINT,
    chat_id    BIGINT,
    text       TEXT,
    created_at TIMESTAMPTZ NOT NULL,
    FOREIGN KEY (author_id) REFERENCES TGUser (id) ON DELETE CASCADE,
    FOREIGN KEY (chat_id) REFERENCES TGChat (id) ON DELETE CASCADE
);