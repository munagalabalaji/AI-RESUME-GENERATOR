import unittest
from app import create_app
from models import db
from models.user import User
from models.resume import Resume
from services.ats_service import ATSService
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # Use in-memory DB for tests
    WTF_CSRF_ENABLED = False

class ResumeGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_user_creation_and_auth(self):
        # Create user
        user = User(name="Test User", email="test@test.com")
        user.set_password("mypassword")
        db.session.add(user)
        db.session.commit()
        
        # Verify database save
        saved_user = User.query.filter_by(email="test@test.com").first()
        self.assertIsNotNone(saved_user)
        self.assertEqual(saved_user.name, "Test User")
        self.assertTrue(saved_user.check_password("mypassword"))
        self.assertFalse(saved_user.check_password("wrongpassword"))

    def test_resume_save_and_ats_score(self):
        # Register user
        user = User(name="Alex", email="alex@email.com")
        user.set_password("alex123")
        db.session.add(user)
        db.session.commit()
        
        # Create resume
        resume = Resume(
            user_id=user.id,
            title="Alex Resume",
            full_name="Alex Carter",
            email="alex@email.com",
            phone="+123456789",
            objective="Develop software",
            summary="Detail-oriented developer experienced in backend tools."
        )
        db.session.add(resume)
        db.session.commit()
        
        # Verify save
        saved_resume = Resume.query.filter_by(title="Alex Resume").first()
        self.assertIsNotNone(saved_resume)
        
        # Calculate ATS score
        ats_result = ATSService.calculate_score(saved_resume)
        self.assertGreater(ats_result['score'], 0)
        self.assertIn('completeness', ats_result['sections'])
        
    def test_login_route(self):
        # Check login page load
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome Back', response.data)

if __name__ == '__main__':
    unittest.main()
