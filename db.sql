CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(320) NULL,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    description TEXT,
    coins INT DEFAULT 0,
    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    creator_id INT,
    description TEXT,
    price INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE friend (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    friend_id INT,
);

CREATE TABLE follower (
    id INT AUTO_INCREMENT PRIMARY KEY,
    follower_id INT,
    followee_id INT,
);

CREATE TABLE game (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    creator_id INT,
    visits INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE `group` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    creator_id INT,
    FOREIGN KEY (creator_id) REFERENCES user(id),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
);


CREATE TABLE group_member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT,
    user_id INT,
    FOREIGN KEY (group_id) REFERENCES `group`(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE session (
    discord_id VARCHAR(255) UNIQUE,
    account_id INT,
    FOREIGN KEY (account_id) REFERENCES user(id)
);
