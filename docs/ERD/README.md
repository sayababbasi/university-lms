erDiagram

    USER {
        int id PK
        string username
        string email
        string password
        string role  // student, teacher, admin, finance
        datetime created_at
        datetime updated_at
    }

    STUDENT {
        int id PK
        int user_id FK
        string reg_no
        string department_id FK
        string batch
        string phone
        string address
    }

    TEACHER {
        int id PK
        int user_id FK
        string designation
        string department_id FK
    }

    DEPARTMENT {
        int id PK
        string name
    }

    COURSE {
        int id PK
        string code
        string title
        string description
        int credit_hours
        int department_id FK
        int teacher_id FK
    }

    LESSON {
        int id PK
        int course_id FK
        string title
        string content_url
    }

    ENROLLMENT {
        int id PK
        int student_id FK
        int course_id FK
        datetime enrolled_at
    }

    ASSIGNMENT {
        int id PK
        int course_id FK
        string title
        string description
        datetime due_date
    }

    SUBMISSION {
        int id PK
        int assignment_id FK
        int student_id FK
        string file_url
        float marks
        datetime submitted_at
    }

    EXAM {
        int id PK
        int course_id FK
        string title
        datetime exam_date
        string type // MCQ, written
    }

    QUESTION {
        int id PK
        int exam_id FK
        string question_text
        string option_a
        string option_b
        string option_c
        string option_d
        string correct_option
    }

    RESULT {
        int id PK
        int exam_id FK
        int student_id FK
        float obtained_marks
        float total_marks
        float gpa
    }

    ATTENDANCE {
        int id PK
        int student_id FK
        int course_id FK
        date date
        boolean status
    }

    INVOICE {
        int id PK
        int student_id FK
        float amount
        float paid_amount
        string status // paid, pending, partial
        datetime created_at
    }

    PAYMENT {
        int id PK
        int invoice_id FK
        float amount
        string payment_gateway // stripe, razorpay
        datetime paid_at
    }

    NOTIFICATION {
        int id PK
        int user_id FK
        string type // email, sms, in-app
        string message
        boolean is_read
        datetime created_at
    }

    USER ||--|{ STUDENT : "has profile"
    USER ||--|{ TEACHER : "has profile"

    DEPARTMENT ||--|{ STUDENT : belongs_to
    DEPARTMENT ||--|{ TEACHER : belongs_to
    DEPARTMENT ||--|{ COURSE : offers

    TEACHER ||--|{ COURSE : teaches
    COURSE ||--|{ LESSON : contains

    STUDENT ||--|{ ENROLLMENT : enrolls
    COURSE ||--|{ ENROLLMENT : has

    COURSE ||--|{ ASSIGNMENT : has
    ASSIGNMENT ||--|{ SUBMISSION : submissions

    COURSE ||--|{ EXAM : has
    EXAM ||--|{ QUESTION : contains
    EXAM ||--|{ RESULT : results
    STUDENT ||--|{ RESULT : has

    STUDENT ||--|{ ATTENDANCE : attendance
    COURSE ||--|{ ATTENDANCE : attendance

    STUDENT ||--|{ INVOICE : billed
    INVOICE ||--|{ PAYMENT : paid

    USER ||--|{ NOTIFICATION : receives
