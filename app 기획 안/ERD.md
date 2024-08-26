erDiagram
    USER {
        int id PK
        string username
        string password
        string full_name
        string email
        string nickname
        string address
        date birth_date
        boolean is_verified
        boolean two_factor_enabled
        string role
        text bio
        string profile_image
        string interests
    }

    POST {
        int id PK
        string title
        text content
        int author_id FK
        datetime created_at
        datetime updated_at
        int likes
        int dislikes
        boolean is_anonymous
        int category_id FK
    }

    COMMENT {
        int id PK
        int post_id FK
        int author_id FK
        text content
        datetime created_at
        datetime updated_at
        int parent_comment_id FK
    }

    VERIFICATIONREQUEST {
        int id PK
        int user_id FK
        string document
        string status
        datetime requested_at
    }

    REACTION {
        int id PK
        int user_id FK
        int post_id FK
        string reaction_type
    }

    DIRECTMESSAGE {
        int id PK
        int sender_id FK
        int recipient_id FK
        text content
        datetime sent_at
        boolean read
    }

    REPORT {
        int id PK
        int user_id FK
        string report_type
        string report_reason
        int post_id FK
        int comment_id FK
        text description
        datetime reported_at
    }

    POSTEDITHISTORY {
        int id PK
        int post_id FK
        int edited_by_id FK
        datetime edit_timestamp
        text previous_content
    }

    CATEGORY {
        int id PK
        string name
    }

    TAG {
        int id PK
        string name
    }

    POST_TAG {
        int post_id PK, FK
        int tag_id PK, FK
    }

    USER ||--o{ POST: "writes"
    USER ||--o{ COMMENT: "writes"
    USER ||--o{ VERIFICATIONREQUEST: "submits"
    USER ||--o{ REACTION: "makes"
    USER ||--o{ DIRECTMESSAGE: "sends"
    USER ||--o{ DIRECTMESSAGE: "receives"
    USER ||--o{ REPORT: "creates"
    POST ||--o{ COMMENT: "receives"
    POST ||--o{ REACTION: "receives"
    POST ||--o{ REPORT: "can be reported in"
    POST ||--o{ POSTEDITHISTORY: "has edits"
    COMMENT ||--o{ COMMENT: "replies to"
    COMMENT ||--o{ REPORT: "can be reported in"
    POST ||--o| CATEGORY: "belongs to"
    POST ||--o{ POST_TAG: "can have many"
    TAG ||--o{ POST_TAG: "can belong to many"

