CREATE TABLE IF NOT EXISTS "webuser" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(255) NOT NULL,
    "disabled" BOOL NOT NULL
);


CREATE INDEX IF NOT EXISTS "idx_webuser_usernam_a9d232" ON "webuser" ("username");