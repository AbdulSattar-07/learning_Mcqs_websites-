# MCQ Learning Platform

A production-ready Django web application for the National Skill Competency Test for IT Graduates. This platform manages 20,000+ Multiple Choice Questions with secure access control and content protection.

## Features

### Public Access
- Browse Domains, Topics, and Subtopics
- View platform information
- Request subscription via WhatsApp integration
- Choose from 7, 15, or 30 days packages

### Paid User Access
- View and practice MCQs
- Filter by Domain, Topic, Subtopic, Batch, Difficulty, Tag
- Search MCQs by keyword
- View answers and explanations
- Paginated results (20 per page)
- Single device login enforcement

### Admin Features
- User management with subscription control
- Subscription request management with one-click approval
- Automatic username/password generation
- WhatsApp-based credential delivery workflow
- Active session monitoring and management
- Force logout capability
- MCQ management (CRUD operations)
- Bulk import from CSV/JSON
- Contact request management
- Domain/Topic/Subtopic management

### Security Features
- Content protection against copying
- Disabled right-click
- Disabled text selection
- Disabled keyboard shortcuts (Ctrl+C, Ctrl+V, Ctrl+X, Ctrl+U, F12, etc.)
- Disabled developer tools shortcuts
- Disabled drag and drop
- Print protection
- Basic developer tools detection

**Note:** Complete screenshot prevention is technically impossible in web browsers. These measures provide strong discouragement against casual copying attempts.

## Technology Stack

- **Backend:** Django 4.2.7
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Database:** SQLite (development), PostgreSQL-ready
- **Authentication:** Django built-in authentication
- **Forms:** django-crispy-forms with Bootstrap 4

## Project Structure

```
mcq_platform/
├── manage.py
├── requirements.txt
├── .env.example
├── sample_data.csv
├── sample_data.json
├── mcq_platform/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── accounts/
│   │   ├── models.py          # CustomUser, ContactRequest
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   └── urls.py
│   └── mcqs/
│       ├── models.py          # Domain, Topic, Subtopic, Batch, MCQ
│       ├── views.py
│       ├── admin.py
│       ├── urls.py
│       └── management/
│           └── commands/
│               └── import_mcqs.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── accounts/
│   │   ├── login.html
│   │   ├── contact.html
│   │   └── contact_success.html
│   └── mcqs/
│       ├── domain_list.html
│       ├── topic_list.html
│       ├── subtopic_list.html
│       ├── mcq_list.html
│       ├── mcq_detail.html
│       └── access_denied.html
└── static/
    ├── css/
    │   ├── style.css
    │   └── mcq_protection.css
    └── js/
        └── mcq_protection.js
```

## Installation

### 1. Clone or Download the Project

```bash
cd mcq_platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` file with your settings:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Usage

### Admin Panel

Access: http://127.0.0.1:8000/admin

1. Login with superuser credentials
2. Create Domains, Topics, Subtopics, Batches
3. Add MCQs manually or import bulk data
4. Create user accounts with paid access
5. Manage contact requests

### Creating Paid Users

1. Go to Admin Panel → Users → Add User
2. Set username and password
3. Set **Access Level** to "Paid"
4. Set **Subscription Status** to "Active"
5. Set **Subscription Expiry** date (future date)
6. Check **Active** checkbox
7. Save

### Importing MCQs

#### From CSV:
```bash
python manage.py import_mcqs sample_data.csv --format=csv
```

#### From JSON:
```bash
python manage.py import_mcqs sample_data.json --format=json
```

#### CSV Format:
```csv
domain,topic,subtopic,batch,difficulty,tag,question_text,option_a,option_b,option_c,option_d,correct_answer,reason
```

#### JSON Format:
```json
[
    {
        "domain": "Programming",
        "topic": "Python",
        "subtopic": "Data Types",
        "batch": "Batch1",
        "difficulty": "Medium",
        "tag": "basics",
        "question_text": "What is...",
        "option_a": "Option A",
        "option_b": "Option B",
        "option_c": "Option C",
        "option_d": "Option D",
        "correct_answer": "A",
        "reason": "Explanation here"
    }
]
```

## Database Models

### CustomUser
- username, email, password
- access_level (Free/Paid)
- subscription_status (Active/Expired/Inactive)
- subscription_expiry
- is_active

### Domain
- name, description

### Topic
- domain (FK), name, description

### Subtopic
- topic (FK), name, description

### Batch
- name, description

### MCQ
- domain, topic, subtopic, batch (FKs)
- difficulty (Easy/Medium/Hard)
- tag
- question_text
- option_a, option_b, option_c, option_d
- correct_answer (A/B/C/D)
- reason

### ContactRequest
- name, email, message
- is_processed

## Performance Optimization

- Database indexes on frequently queried fields
- select_related() for foreign key queries
- prefetch_related() for reverse foreign key queries
- Pagination (20 items per page)
- Optimized for 20,000+ MCQs

## PostgreSQL Configuration

For production, update `.env`:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mcq_platform_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

Then run migrations:
```bash
python manage.py migrate
```

## Security Notes

### Content Protection
The platform implements multiple frontend protection layers:
- CSS user-select: none
- JavaScript event blocking
- Keyboard shortcut disabling
- Right-click prevention
- Developer tools detection

### Important Limitations
- **Screenshots:** Cannot be prevented in browsers
- **Screen recording:** Cannot be prevented in browsers
- **Mobile devices:** Limited protection capabilities
- **Determined users:** Can bypass frontend protections

These measures provide reasonable protection against casual copying but are not foolproof.

### Additional Security Recommendations
1. Use HTTPS in production
2. Implement rate limiting
3. Add session timeout
4. Enable CSRF protection (already enabled)
5. Use strong SECRET_KEY
6. Regular security updates
7. Monitor user activity logs

## Access Control Flow

```
Public User → Browse Domains/Topics/Subtopics
           → Cannot see MCQs
           → Redirected to login if accessing MCQ pages

Logged In (Free) → Can login
                → Cannot see MCQs
                → Shows "Contact administrator" message

Logged In (Paid + Active) → Full MCQ access
                         → Can filter and search
                         → Can view answers/explanations
```

## User Workflow

1. User visits website
2. User browses public content (Domains/Topics/Subtopics)
3. User clicks "Get Access" or "Contact Admin"
4. User fills contact form
5. Admin receives request
6. Admin verifies payment (external process)
7. Admin creates user account with Paid access
8. Admin provides credentials to user
9. User logs in
10. User accesses MCQs

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput
```

### Database errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Import errors
- Check CSV/JSON format matches exactly
- Ensure all required fields are present
- Check for special characters in data

### Permission denied for MCQs
- Verify user access_level is "Paid"
- Verify subscription_status is "Active"
- Verify subscription_expiry is in future
- Verify is_active is True

## Development vs Production

### Development (Current Setup)
- DEBUG=True
- SQLite database
- Django development server
- No HTTPS required

### Production Recommendations
- DEBUG=False
- PostgreSQL database
- Gunicorn/uWSGI server
- Nginx reverse proxy
- HTTPS with SSL certificate
- Environment variables for secrets
- Regular backups
- Monitoring and logging

## License

Proprietary - All rights reserved

## Support

For issues or questions, contact the system administrator.

---

**Version:** 1.0.0  
**Last Updated:** 2024  
**Django Version:** 4.2.7  
**Python Version:** 3.8+
