"""
Populate the Beyond database with test data
Creates 3 employers and multiple candidates with feedback
"""
import os
import sys
from datetime import datetime, date, timedelta

# Add the parent directory to path to import app modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db, Employer, Candidate, Feedback

# Test data
EMPLOYERS = [
    {
        'username': 'techcorp_hr',
        'email': 'hr@techcorp.com',
        'password': 'password123',
        'company_name': 'TechCorp Industries'
    },
    {
        'username': 'innovate_hr',
        'email': 'hiring@innovatesolutions.com',
        'password': 'password123',
        'company_name': 'Innovate Solutions'
    },
    {
        'username': 'global_hr',
        'email': 'hr@globalenterprises.com',
        'password': 'password123',
        'company_name': 'Global Enterprises Inc'
    }
]

CANDIDATES_DATA = [
    # Candidates for TechCorp
    {
        'full_name': 'Sarah Johnson',
        'email': 'sarah.johnson@email.com',
        'phone': '+1-555-0101',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Senior Software Engineer',
                'expertise': 'Python, Django, PostgreSQL, AWS, Docker',
                'feedback_text': 'Sarah was an exceptional engineer who consistently delivered high-quality code. She led the migration of our legacy system to microservices architecture, demonstrating strong technical leadership. Always willing to mentor junior developers and contributed significantly to our code review culture.',
                'rating': 5,
                'employment_start': date(2020, 3, 15),
                'employment_end': date(2023, 8, 30)
            },
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Full Stack Developer',
                'expertise': 'Python, React, Node.js, MongoDB',
                'feedback_text': 'Sarah joined our team and quickly became a valuable contributor. She worked on multiple client projects and received excellent feedback. Her ability to work across the full stack made her very versatile. Left to pursue senior opportunities.',
                'rating': 4,
                'employment_start': date(2018, 6, 1),
                'employment_end': date(2020, 2, 28)
            }
        ]
    },
    {
        'full_name': 'Michael Chen',
        'email': 'michael.chen@email.com',
        'phone': '+1-555-0102',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'DevOps Engineer',
                'expertise': 'Kubernetes, Terraform, CI/CD, Jenkins, AWS',
                'feedback_text': 'Michael transformed our deployment pipeline and reduced deployment time by 70%. His expertise in container orchestration helped us scale efficiently. Proactive in identifying and resolving infrastructure issues. Great team player.',
                'rating': 5,
                'employment_start': date(2021, 1, 10),
                'employment_end': date(2023, 12, 15)
            }
        ]
    },
    {
        'full_name': 'Emily Rodriguez',
        'email': 'emily.rodriguez@email.com',
        'phone': '+1-555-0103',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Product Manager',
                'expertise': 'Agile, JIRA, Product Strategy, Stakeholder Management',
                'feedback_text': 'Emily successfully managed 3 major product launches during her time here. Excellent at gathering requirements and translating them into actionable user stories. Strong communication skills and ability to align technical and business teams. Left for a director-level position.',
                'rating': 4,
                'employment_start': date(2019, 9, 1),
                'employment_end': date(2023, 6, 30)
            },
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Project Manager',
                'expertise': 'Project Management, Agile, Scrum, Risk Management',
                'feedback_text': 'Emily coordinated multiple cross-functional teams effectively. She improved our sprint planning process and increased team velocity by 40%. Professional, organized, and great at managing stakeholder expectations.',
                'rating': 4,
                'employment_start': date(2017, 3, 15),
                'employment_end': date(2019, 7, 31)
            }
        ]
    },
    {
        'full_name': 'David Park',
        'email': 'david.park@email.com',
        'phone': '+1-555-0104',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'QA Engineer',
                'expertise': 'Selenium, Automated Testing, Python, Test Strategy',
                'feedback_text': 'David built our entire test automation framework from scratch. His attention to detail caught many critical bugs before production. Collaborative and always willing to help developers write better tests. Solid contributor.',
                'rating': 4,
                'employment_start': date(2020, 7, 1),
                'employment_end': date(2023, 3, 31)
            }
        ]
    },
    # Candidates for Innovate Solutions
    {
        'full_name': 'Amanda Foster',
        'email': 'amanda.foster@email.com',
        'phone': '+1-555-0201',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'UX/UI Designer',
                'expertise': 'Figma, Adobe XD, User Research, Prototyping, Design Systems',
                'feedback_text': 'Amanda redesigned our entire product interface, resulting in a 50% reduction in user support tickets. Excellent at conducting user research and translating insights into beautiful, intuitive designs. Very collaborative with engineering teams.',
                'rating': 5,
                'employment_start': date(2021, 4, 1),
                'employment_end': date(2023, 11, 30)
            }
        ]
    },
    {
        'full_name': 'Robert Kim',
        'email': 'robert.kim@email.com',
        'phone': '+1-555-0202',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Data Scientist',
                'expertise': 'Python, Machine Learning, TensorFlow, SQL, Data Visualization',
                'feedback_text': 'Robert developed predictive models that improved our customer retention by 30%. Strong analytical skills and ability to communicate complex findings to non-technical stakeholders. His work on our recommendation engine was outstanding.',
                'rating': 5,
                'employment_start': date(2020, 2, 15),
                'employment_end': date(2023, 9, 15)
            },
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Business Analyst',
                'expertise': 'Data Analysis, SQL, Excel, Tableau, Business Intelligence',
                'feedback_text': 'Robert provided excellent analytical support for strategic decisions. He created comprehensive dashboards that became essential tools for management. Detail-oriented and reliable.',
                'rating': 4,
                'employment_start': date(2018, 5, 1),
                'employment_end': date(2020, 1, 31)
            }
        ]
    },
    {
        'full_name': 'Jessica Liu',
        'email': 'jessica.liu@email.com',
        'phone': '+1-555-0203',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Frontend Developer',
                'expertise': 'React, TypeScript, CSS, Redux, Jest',
                'feedback_text': 'Jessica was our go-to person for complex UI challenges. She optimized our web app performance significantly and mentored other frontend developers. Strong code quality and attention to accessibility standards.',
                'rating': 4,
                'employment_start': date(2021, 8, 1),
                'employment_end': date(2023, 10, 31)
            }
        ]
    },
    {
        'full_name': 'Thomas Wright',
        'email': 'thomas.wright@email.com',
        'phone': '+1-555-0204',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Security Engineer',
                'expertise': 'Cybersecurity, Penetration Testing, OWASP, Network Security',
                'feedback_text': 'Thomas strengthened our security posture significantly. He conducted regular security audits and trained the team on security best practices. Identified and resolved several critical vulnerabilities. Professional and thorough.',
                'rating': 5,
                'employment_start': date(2022, 1, 10),
                'employment_end': date(2023, 12, 20)
            }
        ]
    },
    # Candidates for Global Enterprises
    {
        'full_name': 'Rachel Martinez',
        'email': 'rachel.martinez@email.com',
        'phone': '+1-555-0301',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Sales Manager',
                'expertise': 'B2B Sales, CRM, Salesforce, Negotiation, Team Leadership',
                'feedback_text': 'Rachel exceeded her sales targets for 3 consecutive years. Built strong client relationships and expanded our enterprise client base by 40%. Excellent leadership skills and motivated her team effectively. A true sales professional.',
                'rating': 5,
                'employment_start': date(2019, 6, 1),
                'employment_end': date(2023, 8, 31)
            }
        ]
    },
    {
        'full_name': 'Kevin Anderson',
        'email': 'kevin.anderson@email.com',
        'phone': '+1-555-0302',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Backend Engineer',
                'expertise': 'Java, Spring Boot, Microservices, MySQL, Kafka',
                'feedback_text': 'Kevin designed and implemented several critical microservices for our platform. Clean code, good documentation, and solid understanding of scalability challenges. Reliable and meets deadlines consistently.',
                'rating': 4,
                'employment_start': date(2020, 9, 1),
                'employment_end': date(2023, 11, 30)
            },
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Software Developer',
                'expertise': 'Java, REST APIs, Spring Framework, Git',
                'feedback_text': 'Kevin was a dependable developer who contributed to several key projects. Good problem-solving skills and quick learner. Left to pursue backend specialization opportunities.',
                'rating': 3,
                'employment_start': date(2019, 1, 15),
                'employment_end': date(2020, 8, 15)
            }
        ]
    },
    {
        'full_name': 'Lisa Thompson',
        'email': 'lisa.thompson@email.com',
        'phone': '+1-555-0303',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'HR Manager',
                'expertise': 'Talent Acquisition, Employee Relations, HR Strategy, Compliance',
                'feedback_text': 'Lisa streamlined our hiring process and reduced time-to-hire by 35%. She implemented excellent employee engagement programs and maintained high team morale. Professional, empathetic, and strategic in her approach.',
                'rating': 5,
                'employment_start': date(2021, 3, 1),
                'employment_end': date(2023, 10, 31)
            }
        ]
    },
    {
        'full_name': 'Daniel Brooks',
        'email': 'daniel.brooks@email.com',
        'phone': '+1-555-0304',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Marketing Manager',
                'expertise': 'Digital Marketing, SEO, Content Strategy, Google Analytics, Social Media',
                'feedback_text': 'Daniel led several successful marketing campaigns that increased our online presence significantly. Creative thinker with strong analytical skills. His content strategy improved our organic traffic by 120%. Great team collaborator.',
                'rating': 4,
                'employment_start': date(2020, 4, 15),
                'employment_end': date(2023, 7, 31)
            }
        ]
    },
    # Indian Employees
    {
        'full_name': 'Priya Sharma',
        'email': 'priya.sharma@email.com',
        'phone': '+91-9876543210',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Senior Java Developer',
                'expertise': 'Java, Spring Boot, Microservices, Kafka, Redis, MySQL',
                'feedback_text': 'Priya was instrumental in developing our payment processing system. Her deep knowledge of Java and microservices architecture helped us build a highly scalable solution. Excellent problem solver and mentor to junior developers. Very dedicated and professional.',
                'rating': 5,
                'employment_start': date(2019, 8, 1),
                'employment_end': date(2023, 9, 30)
            },
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Software Engineer',
                'expertise': 'Java, REST APIs, Spring Framework, Hibernate',
                'feedback_text': 'Priya was a strong contributor to our backend services. She consistently delivered high-quality code and was great at code reviews. Left to pursue senior opportunities.',
                'rating': 4,
                'employment_start': date(2017, 6, 15),
                'employment_end': date(2019, 7, 15)
            }
        ]
    },
    {
        'full_name': 'Rahul Patel',
        'email': 'rahul.patel@email.com',
        'phone': '+91-9876543211',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Frontend Architect',
                'expertise': 'React, Next.js, TypeScript, GraphQL, Webpack, Performance Optimization',
                'feedback_text': 'Rahul led the frontend architecture redesign that improved our page load times by 60%. Outstanding technical skills and leadership. He established best practices for our entire frontend team and conducted excellent technical interviews. A real asset to any organization.',
                'rating': 5,
                'employment_start': date(2020, 3, 1),
                'employment_end': date(2023, 10, 31)
            }
        ]
    },
    {
        'full_name': 'Anjali Reddy',
        'email': 'anjali.reddy@email.com',
        'phone': '+91-9876543212',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Product Owner',
                'expertise': 'Product Management, User Stories, Agile, Roadmap Planning, Market Analysis',
                'feedback_text': 'Anjali successfully managed our flagship product and increased user engagement by 45%. She has excellent stakeholder management skills and deeply understands customer needs. Her product roadmap was well-received by both technical teams and executives. Highly recommended.',
                'rating': 5,
                'employment_start': date(2021, 1, 15),
                'employment_end': date(2023, 11, 15)
            }
        ]
    },
    {
        'full_name': 'Vikram Singh',
        'email': 'vikram.singh@email.com',
        'phone': '+91-9876543213',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'DevOps Lead',
                'expertise': 'AWS, Kubernetes, Docker, Terraform, Ansible, CI/CD Pipelines',
                'feedback_text': 'Vikram transformed our infrastructure to cloud-native architecture. He reduced our deployment time from hours to minutes and improved system reliability to 99.9% uptime. Excellent leadership and technical expertise. Always proactive in identifying and resolving issues.',
                'rating': 5,
                'employment_start': date(2020, 9, 1),
                'employment_end': date(2023, 12, 10)
            },
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Systems Engineer',
                'expertise': 'Linux, Shell Scripting, Monitoring, AWS',
                'feedback_text': 'Vikram maintained our production systems with zero major incidents during his tenure. Reliable, skilled, and quick to respond to issues. Good team player.',
                'rating': 4,
                'employment_start': date(2018, 4, 1),
                'employment_end': date(2020, 8, 15)
            }
        ]
    },
    {
        'full_name': 'Sneha Gupta',
        'email': 'sneha.gupta@email.com',
        'phone': '+91-9876543214',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Mobile App Developer',
                'expertise': 'React Native, iOS, Android, Mobile UI/UX, Firebase',
                'feedback_text': 'Sneha developed our mobile app from scratch which now has over 100K downloads with 4.5+ rating. She has strong mobile development skills and great attention to detail. The app performance and user experience are excellent thanks to her work.',
                'rating': 5,
                'employment_start': date(2021, 5, 1),
                'employment_end': date(2023, 10, 20)
            }
        ]
    },
    {
        'full_name': 'Arjun Kumar',
        'email': 'arjun.kumar@email.com',
        'phone': '+91-9876543215',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Machine Learning Engineer',
                'expertise': 'Python, TensorFlow, PyTorch, NLP, Computer Vision, MLOps',
                'feedback_text': 'Arjun built our ML-powered recommendation system that increased customer engagement by 35%. Strong understanding of both ML theory and practical implementation. He also established our ML pipeline and best practices. Excellent communicator who can explain complex concepts simply.',
                'rating': 5,
                'employment_start': date(2021, 7, 1),
                'employment_end': date(2023, 11, 30)
            }
        ]
    },
    {
        'full_name': 'Pooja Desai',
        'email': 'pooja.desai@email.com',
        'phone': '+91-9876543216',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Scrum Master',
                'expertise': 'Agile Coaching, Scrum, Team Facilitation, Jira, Confluence',
                'feedback_text': 'Pooja was an excellent Scrum Master who helped our teams adopt agile practices effectively. She improved team velocity by 50% and created a collaborative environment. Great at removing blockers and coaching team members. Very organized and professional.',
                'rating': 5,
                'employment_start': date(2020, 11, 1),
                'employment_end': date(2023, 9, 30)
            },
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Project Coordinator',
                'expertise': 'Project Management, Agile, Communication, Documentation',
                'feedback_text': 'Pooja coordinated multiple projects efficiently. Good organizational skills and ability to keep teams on track. Professional and reliable.',
                'rating': 4,
                'employment_start': date(2019, 2, 1),
                'employment_end': date(2020, 10, 15)
            }
        ]
    },
    {
        'full_name': 'Karthik Menon',
        'email': 'karthik.menon@email.com',
        'phone': '+91-9876543217',
        'feedbacks': [
            {
                'employer_idx': 1,  # Innovate Solutions
                'role': 'Full Stack Engineer',
                'expertise': 'Node.js, React, MongoDB, Express, GraphQL, Docker',
                'feedback_text': 'Karthik is a versatile engineer who can handle both frontend and backend work effectively. He built several critical features for our SaaS platform. Clean code, good testing practices, and collaborative approach. Would definitely hire again.',
                'rating': 4,
                'employment_start': date(2020, 6, 1),
                'employment_end': date(2023, 8, 31)
            }
        ]
    },
    {
        'full_name': 'Divya Krishnan',
        'email': 'divya.krishnan@email.com',
        'phone': '+91-9876543218',
        'feedbacks': [
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Cloud Solutions Architect',
                'expertise': 'AWS, Azure, Cloud Architecture, Serverless, Solution Design',
                'feedback_text': 'Divya designed our multi-cloud strategy and led the migration of legacy applications to the cloud. Outstanding architectural skills and deep cloud expertise. She saved us 40% on infrastructure costs while improving performance. Exceptional professional.',
                'rating': 5,
                'employment_start': date(2021, 2, 1),
                'employment_end': date(2023, 12, 15)
            },
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Solutions Engineer',
                'expertise': 'AWS, Cloud Infrastructure, Technical Consulting',
                'feedback_text': 'Divya provided excellent technical consulting for our cloud migration projects. Strong technical knowledge and good client communication skills. Delivered projects on time.',
                'rating': 4,
                'employment_start': date(2019, 7, 1),
                'employment_end': date(2021, 1, 15)
            }
        ]
    },
    {
        'full_name': 'Rohit Malhotra',
        'email': 'rohit.malhotra@email.com',
        'phone': '+91-9876543219',
        'feedbacks': [
            {
                'employer_idx': 2,  # Global Enterprises
                'role': 'Technical Lead',
                'expertise': 'Team Leadership, System Design, Python, Microservices, Mentoring',
                'feedback_text': 'Rohit led a team of 8 engineers and delivered multiple complex projects successfully. Excellent technical and leadership skills. He mentored junior developers effectively and maintained high code quality standards. Great at architecture discussions and making sound technical decisions.',
                'rating': 5,
                'employment_start': date(2020, 1, 15),
                'employment_end': date(2023, 11, 30)
            },
            {
                'employer_idx': 0,  # TechCorp
                'role': 'Senior Software Engineer',
                'expertise': 'Python, Django, REST APIs, PostgreSQL',
                'feedback_text': 'Rohit was a strong senior engineer who delivered consistently. Good technical skills and ability to work independently. Left for a leadership role.',
                'rating': 4,
                'employment_start': date(2018, 3, 1),
                'employment_end': date(2019, 12, 31)
            }
        ]
    }
]


def populate_database():
    """Populate the database with test data"""
    with app.app_context():
        print("🗑️  Clearing existing data...")
        # Clear existing data
        Feedback.query.delete()
        Candidate.query.delete()
        Employer.query.delete()
        db.session.commit()
        
        print("\n👥 Creating employers...")
        employers = []
        for emp_data in EMPLOYERS:
            employer = Employer(
                username=emp_data['username'],
                email=emp_data['email'],
                company_name=emp_data['company_name']
            )
            employer.set_password(emp_data['password'])
            db.session.add(employer)
            employers.append(employer)
            print(f"   ✓ Created: {emp_data['company_name']} ({emp_data['username']})")
        
        db.session.commit()
        
        print("\n📋 Creating candidates and feedback...")
        candidate_count = 0
        feedback_count = 0
        
        for candidate_data in CANDIDATES_DATA:
            # Create candidate
            candidate = Candidate(
                full_name=candidate_data['full_name'],
                email=candidate_data['email'],
                phone=candidate_data['phone']
            )
            db.session.add(candidate)
            db.session.flush()
            candidate_count += 1
            
            print(f"\n   👤 {candidate.full_name} ({candidate.email})")
            
            # Add feedback from employers
            for feedback_data in candidate_data['feedbacks']:
                employer = employers[feedback_data['employer_idx']]
                feedback = Feedback(
                    candidate_id=candidate.id,
                    employer_id=employer.id,
                    role=feedback_data['role'],
                    expertise=feedback_data['expertise'],
                    feedback_text=feedback_data['feedback_text'],
                    rating=feedback_data['rating'],
                    employment_start=feedback_data['employment_start'],
                    employment_end=feedback_data['employment_end']
                )
                db.session.add(feedback)
                feedback_count += 1
                print(f"      └─ Feedback from {employer.company_name} as {feedback_data['role']} ({feedback_data['rating']}★)")
        
        db.session.commit()
        
        print(f"\n✅ Database populated successfully!")
        print(f"   📊 Created: {len(employers)} employers, {candidate_count} candidates, {feedback_count} feedback entries")
        
        print("\n" + "="*60)
        print("🔐 LOGIN CREDENTIALS")
        print("="*60)
        for emp_data in EMPLOYERS:
            print(f"\nCompany: {emp_data['company_name']}")
            print(f"Username: {emp_data['username']}")
            print(f"Password: {emp_data['password']}")
            print(f"Email: {emp_data['email']}")
        print("\n" + "="*60)


if __name__ == '__main__':
    print("🚀 Starting database population...")
    print("="*60)
    populate_database()
    print("\n✨ Done! You can now login with any of the accounts above.")
    print("   Visit: http://127.0.0.1:5001")

