from app import create_app
from models import db
from models.user import User
from models.resume import Resume, Education, Experience, Project, Skill, Certification, Achievement, Language
from models.audit import AuditLog

def seed():
    app = create_app()
    with app.app_context():
        # Check if test user exists
        test_email = "user@resumegen.com"
        user = User.query.filter_by(email=test_email).first()
        
        if not user:
            user = User(
                name="John Doe",
                email=test_email,
                role="user"
            )
            user.set_password("user123")
            db.session.add(user)
            db.session.commit()
            print(f"Created test user: {test_email}")
        
        # Check if user has any resumes
        if len(user.resumes) == 0:
            # Create a sample complete resume
            resume = Resume(
                user_id=user.id,
                title="Sample Full-Stack Developer Resume",
                template="modern",
                full_name="John Doe",
                email=test_email,
                phone="+1 (555) 987-6543",
                address="101 Digital Boulevard, Austin, TX",
                linkedin="linkedin.com/in/johndoe",
                github="github.com/johndoe",
                portfolio="johndoe.dev",
                objective="Results-driven and highly creative Software Engineer with 4+ years of experience specializing in backend architectures, RESTful API design, and containerized deployments. Looking to leverage full-stack skills to build impactful features at a scaling tech firm.",
                summary="Passionate developer specializing in Python/Flask and JavaScript/React. Experienced in designing microservices, optimizing SQL databases, and setting up CI/CD pipelines. Active open-source contributor.",
                hobbies="Coding, open-source projects, playing chess, digital photography"
            )
            db.session.add(resume)
            db.session.flush() # Flush to get resume.id
            
            # 1. Add Education
            db.session.add(Education(
                resume_id=resume.id,
                degree="Bachelor of Science",
                branch="Computer Science",
                institution="University of Texas at Austin",
                university="UT System",
                cgpa="3.7/4.0",
                start_year="2016",
                end_year="2020"
            ))
            
            # 2. Add Experience
            db.session.add(Experience(
                resume_id=resume.id,
                company="Apex Web Solutions",
                role="Backend Software Engineer",
                duration="Jun 2020 - Present",
                responsibilities="* Spearheaded design and integration of backend microservices using Flask, cutting API response latency by 35%.\n* Designed and optimized PostgreSQL database schema, resulting in 20% faster read operations on analytics routes.\n* Managed deployments using Docker containers on AWS ECS, coordinating smooth releases under agile sprints."
            ))
            
            # 3. Add Projects
            db.session.add(Project(
                resume_id=resume.id,
                name="SaaS Task Management API",
                description="Designed and deployed a multitenant task management system. Set up automated email reminders, JWT-based secure authorization, and Stripe billing integrations.",
                technologies="Python, Flask, PostgreSQL, Redis, Celery, Docker",
                github_link="github.com/johndoe/task-api",
                live_demo="api.tasksaas.com"
            ))
            db.session.add(Project(
                resume_id=resume.id,
                name="Developer Portfolio Portal",
                description="Built a highly responsive responsive portfolio frontend incorporating dark/light theme switching, contact form API triggers, and visual project showcases.",
                technologies="HTML5, CSS3, JavaScript, React, Tailwind CSS",
                github_link="github.com/johndoe/portfolio",
                live_demo="johndoe.dev"
            ))
            
            # 4. Add Skills
            skills_data = [
                ("Python", "Technical"),
                ("JavaScript", "Technical"),
                ("SQL", "Technical"),
                ("Flask", "Framework"),
                ("React", "Framework"),
                ("Docker", "Tool"),
                ("AWS ECS", "Tool"),
                ("Git", "Tool"),
                ("Agile Scrums", "Soft"),
                ("Problem Solving", "Soft")
            ]
            for name, stype in skills_data:
                db.session.add(Skill(resume_id=resume.id, name=name, skill_type=stype))
                
            # 5. Add Certifications
            db.session.add(Certification(
                resume_id=resume.id,
                name="AWS Certified Solutions Architect -- Associate",
                organization="Amazon Web Services",
                date_obtained="Jan 2023",
                credential_url="aws.verify.com/architect-associate-id"
            ))
            
            # 6. Add Achievements
            db.session.add(Achievement(
                resume_id=resume.id,
                description="Recognized as Employee of the Quarter (Q2 2024) for leading high-priority api integrations under budget."
            ))
            
            # 7. Add Languages
            db.session.add(Language(
                resume_id=resume.id,
                name="English",
                proficiency="Native"
            ))
            db.session.add(Language(
                resume_id=resume.id,
                name="Spanish",
                proficiency="Intermediate"
            ))
            
            db.session.commit()
            print("Successfully seeded database with complete sample resume!")
            
            # Log audit
            log = AuditLog(
                user_id=user.id,
                action="Database Seeding",
                details="Automatically seeded mock profile and sample developer resume"
            )
            db.session.add(log)
            db.session.commit()
        else:
            print("User already has resumes. Seeding skipped.")

if __name__ == '__main__':
    seed()
