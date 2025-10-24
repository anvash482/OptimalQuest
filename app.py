from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import json
import os 
from werkzeug.utils import secure_filename
import os
import datetime

app = Flask(__name__)
app.secret_key = "Creation#1anvayashwin2010!"
with open("career_Paths.json") as f:
    CAREER_PATHS = json.load(f)

# ✅ Make sure the log file always works, no matter where the app runs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "logins.txt")

# ✅ Create the logins.txt file if it doesn’t exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("=== Login Log File ===\n")
    
profiles = {}


subjects = [
    "Mathematics",
    "Computer Science",
    "Physics",
    "Chemistry",
    "Biology",
    "English / Literature",
    "History / Social Studies",
    "Economics",
    "Art / Visual Arts",
    "Graphic Design / Digital Media",
    "Marketing / Business Studies",
    "Psychology",
    "Communication / Public Speaking",
    "Music / Performing Arts",
    "Engineering / Design Technology"
]

users = {}
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            flash("Please login to access the page", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/courses')
def courses():
    return render_template('pages/courses.html')

@app.route('/courseslinks.html')
def courseslinks():
    return render_template('courseslinks.html')

@app.route('/careers')
def careers():
    return render_template('pages/careers.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('logged_out'))

@app.route('/logged_out')
def logged_out():
    return render_template('pages/logout.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/techcourses')
def techcourses():
    return render_template('techcourses.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm_password", "")

        if not username or not password:
            flash("Username or password required", "danger")
            return redirect(url_for("register"))

        if password != confirm:
            flash("Password does not match", "danger")
            return redirect(url_for("register"))

        if username in users:
            flash("Username already taken", "danger")
            return redirect(url_for("register"))

        password_hash = generate_password_hash(password, method="pbkdf2:sha256")
        users[username] = {"password_hash": password_hash}
        flash("Registration successful, please login", "success")
        return redirect(url_for("login"))

    return render_template("pages/register.html")



@app.route('/login', methods=["GET", "POST"])
def login():
    next_page = request.args.get("next")

    if request.method == "POST":
        username  = request.form.get("username", "").strip().lower()
        password  = request.form.get("password", "")
        next_page = request.form.get("next")  # from hidden field

        user = users.get(username)

        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid credentials", "danger")
            return redirect(url_for("login", next=next_page))

        # ✅ Successful login
        session["user"] = username
        flash(f"Welcome, {username}!", "success")

        # ✅ Log successful login with timestamp
        with open(LOG_FILE, "a") as f:
            f.write(f"{username} logged in at {datetime.datetime.now()}\n")

        return redirect(next_page or url_for("dashboard"))

    return render_template("pages/login.html", next_page=next_page or "")


@app.route('/softwaredeveloper')
@login_required
def softwaredeveloper():
    return render_template('careers/softwaredeveloper.html')

@app.route('/datascientist')
@login_required
def datascientist():
    return render_template('careers/datascientist.html')

@app.route('/machinelearning')
@login_required
def machinelearning():
    return render_template('careers/machinelearning.html')

@app.route('/frontenddeveloper')
@login_required
def frontenddeveloper():
    return render_template('careers/frontenddeveloper.html')

@app.route('/gamedeveloper')
@login_required
def gamedeveloper():
    return render_template('careers/gamedeveloper.html')

@app.route('/appdeveloper')
@login_required
def appdeveloper():
    return render_template('careers/appdeveloper.html')

@app.route('/cybersecurityanalysist')
@login_required
def cybersecurityanalysist():
    return render_template('careers/cybersecurityanalysist.html')

@app.route('/airesearcher')
@login_required
def airesearcher():
    return render_template('careers/airesearcher.html')

@app.route('/ux_uidesigner')
@login_required
def ux_uidesigner():
    return render_template('careers/ux_uidesigner.html')

@app.route('/dataanalyst')
@login_required
def dataanalyst():
    return render_template('careers/dataanalyst.html')

@app.route('/bia')
@login_required
def bia():
    return render_template('careers/bia.html')

@app.route('/statistician')
@login_required
def statistician():
    return render_template('careers/statistician.html')

@app.route('/finana')
@login_required
def finana():
    return render_template('careers/finana.html')

@app.route('/mra')
@login_required
def mra():
    return render_template('careers/mra.html')

@app.route('/operationsanalyst')
@login_required
def operationsanalyst():
    return render_template('careers/operationsanalyst.html')

@app.route('/actuary')
@login_required
def actuary():
    return render_template('careers/actuary.html')


@app.route('/gd')
@login_required
def gd():
    return render_template('careers/gd.html')

@app.route('/videoeditor')
@login_required
def videoeditor():
    return render_template('careers/videoeditor.html')

@app.route('/ux_designer')
@login_required
def ux_designer():
    return render_template('careers/ux_designer.html')

@app.route('/ui_designer')
@login_required
def ui_designer():
    return render_template('careers/ui_designer.html')

@app.route('/animator')
@login_required
def animator():
    return render_template('careers/animator.html')

@app.route('/artdirector')
@login_required
def artdirector():
    return render_template('careers/artdirector.html')

@app.route('/creativetechnologist')
@login_required
def creativetechnologist():
    return render_template('careers/creativetechnologist.html')

@app.route('/socialmediamanager')
@login_required
def socialmediamanager():
    return render_template('careers/socialmediamanager.html')

@app.route('/technicalwriter')
@login_required
def technicalwriter():
    return render_template('careers/technicalwriter.html')

@app.route('/policy_analyst')
@login_required
def policy_analyst():
    return render_template('careers/policy_analyst.html')

@app.route('/industrialdesigner')
@login_required
def industrialdesigner():
    return render_template('careers/industrialdesigner.html')

@app.route('/contentwriter')
@login_required
def contentwriter():
    return render_template('careers/contentwriter.html')

@app.route('/copywriter')
@login_required
def copywriter():
    return render_template('careers/copywriter.html')

@app.route('/journalist')
@login_required
def journalist():
    return render_template('careers/journalist.html')

@app.route('/podcast_producer')
@login_required
def podcast_producer():
    return render_template('careers/podcast_producer.html')

@app.route('/academic_researcher')
@login_required
def academic_researcher():
    return render_template('careers/academic_researcher.html')

@app.route('/scientist')
@login_required
def scientist():
    return render_template('careers/scientist.html')

@app.route('/university_professor')
@login_required
def university_professor():
    return render_template('careers/university_professor.html')

@app.route('/policy_anaylist')
@login_required
def policy_anaylist():
    return render_template('careers/policy_anaylist.html')

@app.route('/environmental_researcher')
@login_required
def environmental_researcher():
    return render_template('careers/environmental_researcher.html')

@app.route('/psychology')
@login_required
def psychology():
    return render_template('careers/psychology.html')

@app.route('/entrepreneur')
@login_required
def entrepreneur():
    return render_template('careers/entrepreneur.html')

@app.route('/product_manager')
@login_required
def product_manager():
    return render_template('careers/product_manager.html')

@app.route('/marketing_manager')
@login_required
def marketing_manager():
    return render_template('careers/marketing_manager.html')

# Social Impact & Nonprofit
@app.route('/management_consultant')
@login_required
def management_consultant():
    return render_template('careers/management_consultant.html')

@app.route('/business_analyst')
@login_required
def business_analyst():
    return render_template('careers/business_analyst.html')

@app.route('/sales_strategist')
@login_required
def sales_strategist():
    return render_template('careers/sales_strategist.html')

@app.route('/ecommerce_manager')
@login_required
def ecommerce_manager():
    return render_template('careers/ecommerce_manager.html')

@app.route('/social_worker')
@login_required
def social_worker():
    return render_template('careers/social_worker.html')

@app.route('/ngo_project_manager')
@login_required
def ngo_project_manager():
    return render_template('careers/ngo_project_manager.html')

@app.route('/public_health_specialist')
@login_required
def public_health_specialist():
    return render_template('careers/public_health_specialist.html')

@app.route('/education_program_manager')
@login_required
def education_program_manager():
    return render_template('careers/education_program_manager.html')

@app.route('/community_organizer')
@login_required
def community_organizer():
    return render_template('careers/community_organizer.html')

@app.route('/mental_health_counselor')
@login_required
def mental_health_counselor():
    return render_template('careers/mental_health_counselor.html')

@app.route('/youth_mentor')
@login_required
def youth_mentor():
    return render_template('careers/youth_mentor.html')


# Healthcare & Medicine
@app.route('/nurse')
@login_required
def nurse():
    return render_template('careers/nurse.html')

@app.route('/psychologist')
@login_required
def psychologist():
    return render_template('careers/psychologist.html')

@app.route('/physical_therapist')
@login_required
def physical_therapist():
    return render_template('careers/physical_therapist.html')

@app.route('/nutritionist')
@login_required
def nutritionist():
    return render_template('careers/nutritionist.html')

@app.route('/occupational_therapist')
@login_required
def occupational_therapist():
    return render_template('careers/occupational_therapist.html')

@app.route('/health_tech_innovator')
@login_required
def health_tech_innovator():
    return render_template('careers/health_tech_innovator.html')

@app.route('/general_practitioner')
@login_required
def general_practitioner():
    return render_template('careers/general_practitioner.html')

@app.route('/pediatrician')
@login_required
def pediatrician():
    return render_template('careers/pediatrician.html')

@app.route('/cardiologist')
@login_required
def cardiologist():
    return render_template('careers/cardiologist.html')

@app.route('/neurologist')
@login_required
def neurologist():
    return render_template('careers/neurologist.html')

@app.route('/dermatologist')
@login_required
def dermatologist():
    return render_template('careers/dermatologist.html')

@app.route('/orthopedic_surgeon')
@login_required
def orthopedic_surgeon():
    return render_template('careers/orthopedic_surgeon.html')

@app.route('/curriculum_designer')
@login_required
def curriculum_designer():
    return render_template('careers/curriculum_designer.html')

@app.route('/oncologist')
@login_required
def oncologist():
    return render_template('careers/oncologist.html')

@app.route('/psychiatrist')
@login_required
def psychiatrist():
    return render_template('careers/psychiatrist.html')

@app.route('/ophthalmologist')
@login_required
def ophthalmologist():
    return render_template('careers/ophthalmologist.html')

@app.route('/surgeon_general')
@login_required
def surgeon_general():
    return render_template('careers/surgeon_general.html')

@app.route('/radiologist')
@login_required
def radiologist():
    return render_template('careers/radiologist.html')

@app.route('/pathologist')
@login_required
def pathologist():
    return render_template('careers/pathologist.html')

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/obgyn')
@login_required
def obgyn():
    return render_template('careers/obgyn.html')

@app.route('/anesthesiologist')
@login_required
def anesthesiologist():
    return render_template('careers/anesthesiologist.html')

@app.route('/emergency_medicine_doctor')
@login_required
def emergency_medicine_doctor():
    return render_template('careers/emergency_medicine_doctor.html')


# Education & Training
@app.route('/school_teacher')
@login_required
def school_teacher():
    return render_template('careers/school_teacher.html')


@app.route('/college_counselor')
@login_required
def college_counselor():
    return render_template('careers/college_counselor.html')

@app.route('/online_course_creator')
@login_required
def online_course_creator():
    return render_template('careers/online_course_creator.html')

@app.route('/education_technologist')
@login_required
def education_technologist():
    return render_template('careers/education_technologist.html')


# Lifestyle & Independent Careers
@app.route('/freelance_designer_developer')
@login_required
def freelance_designer_developer():
    return render_template('careers/freelance_designer_developer.html')

@app.route('/youtuber_content_creator')
@login_required
def youtuber_content_creator():
    return render_template('careers/youtuber_content_creator.html')

@app.route('/digital_nomad_remote_worker')
@login_required
def digital_nomad_remote_worker():
    return render_template('careers/digital_nomad_remote_worker.html')

@app.route('/author')
@login_required
def author():
    return render_template('careers/author.html')

@app.route('/life_coach')
@login_required
def life_coach():
    return render_template('careers/life_coach.html')

@app.route('/travel_blogger')
@login_required
def travel_blogger():
    return render_template('careers/travel_blogger.html')

@app.route('/prspecialist')
@login_required
def prspecialist():
    return render_template('careers/prspecialist.html')

@app.route('/dataandanalysis')
@login_required
def dataandanalysis():
    return render_template('courses/dataandanalysis.html')

@app.route('/creativeanddesign')
@login_required
def creativeanddesign():
    return render_template('courses/creativeanddesign.html')

@app.route('/communicationsandwriting')
@login_required
def communicationsandwriting():
    return render_template('courses/communicationsandwriting.html')


@app.route('/researchandacademia')
@login_required
def researchandacademia():
    return render_template('courses/researchandacademia.html')

@app.route('/bussinessandentreprenuership')
@login_required
def bussinessandentreprenuership():
    return render_template('courses/bussinessandentreprenuership.html')

@app.route('/socialimpactandnonprofit')
@login_required
def socialimpactandnonprofit():
    return render_template('courses/socialimpactandnonprofit.html')

@app.route('/healthcareandwellness')
@login_required
def healthcareandwellness():
    return render_template('courses/healthcareandwellness.html')

@app.route('/medicalspecialization')
@login_required
def medicalspecialization():
    return render_template('courses/medicalspecialization.html')

@app.route('/educationandtraining')
@login_required
def educationandtraining():
    return render_template('courses/educationandtraining.html')

# -----------------------
# 1. Subject Selection
# -----------------------
@app.route('/quizpage1', methods=["GET", "POST"])
@login_required
def quizpage1():
    if request.method == "POST":
        selected_subjects = request.form.get("subjects", "").split(",")
        selected_subjects = [s for s in selected_subjects if s]

        if 2 <= len(selected_subjects) <= 5:
            session["selected_subjects"] = selected_subjects
            return redirect(url_for("quizpage2"))
        else:
            flash("Please select between 2 and 5 subjects.", "warning")
            return redirect(url_for('quizpage1'))

    return render_template('quiz/quizpage1.html', subjects=subjects)

# -----------------------
# 2. Enter Grades for Subjects
# -----------------------
@app.route('/quizpage2', methods=["GET", "POST"])
@login_required
def quizpage2():
    selected_subjects = session.get("selected_subjects", [])

    if request.method == "POST":
        grades = {}
        total_gpa = 0

        grade_to_gpa = {1: 0.0, 2: 1.0, 3: 2.0, 4: 3.0, 5: 4.0}

        for subj in selected_subjects:
            # Get the grade from the form and convert to int
            grade = int(request.form.get(subj, 0))
            grades[subj] = grade
            total_gpa += grade_to_gpa.get(grade, 0)

        # Calculate average GPA
        gpa = round(total_gpa / len(selected_subjects), 2) if selected_subjects else 0.0

        # Save in session
        session["grades"] = grades
        session["gpa"] = gpa

        return redirect(url_for("extracurriculars"))

    return render_template("quiz/quizpage2.html", selected_subjects=selected_subjects)
# -----------------------
# 3. Save Extracurriculars
# -----------------------

@app.route("/extracurriculars", methods=["GET", "POST"])
@login_required
def extracurriculars():
    if request.method == "POST":
        extracurriculars = request.form.getlist("extracurriculars")
        session["extracurriculars"] = extracurriculars
        return redirect(url_for("actualquizpage1"))
    return render_template("quiz/extracurriculars.html")

@app.route('/actualquizpage1')
@login_required
def actualquizpage1():
    return render_template('quiz/actualquizpage1.html')

@app.route("/submit_quiz", methods=["POST"])
@login_required
def submit_quiz():
    answers = []
    for i in range(1, 16):
        val = request.form.get(f"q{i}")
        if val:
            answers.append(val)


    if not answers:
        print("No answers received! Check your form submission.")
        flash("Please answer all questions.", "warning")
        return redirect(url_for("actualquizpage1"))


    mapping = {"A": "Thinker", "B": "Creator", "C": "Helper", "D": "Leader"}
    personality_answers = [{"trait": mapping.get(ans, "Thinker")} for ans in answers]
    session["personality_answers"] = personality_answers


    print("Personality Answers Saved:", personality_answers)
    return redirect(url_for("results"))


@app.route('/techandengierring')
@login_required
def techandengierring():
    return render_template('courses/techandengierring.html')


@app.route("/results")
@login_required
def results():
    # --- Fetch session data safely ---
    selected_subjects = [s.strip().lower() for s in session.get("selected_subjects", [])]
    gpa = float(session.get("gpa", 0))
    extracurriculars = session.get("extracurriculars", []) or []
    personality_answers = session.get("personality_answers", [])

    # --- 1️⃣ Stream detection (allow multiple matches and partial match) ---
    stream_mapping = {
        "Tech & Engineering": ["computer science", "math", "engineering", "it", "design", "design technology"],
        "Science & Medical": ["biology", "chemistry", "physics", "health science", "biotech"],
        "Humanities & Social Studies": ["english", "history", "political science", "media", "psychology", "sociology", "journalism"],
        "Creative & Design": ["art", "film", "music", "visual arts", "fine arts", "design", "animation", "design technology"],
        "Business & Management": ["business", "economics", "commerce", "accounting", "finance", "management", "marketing"]
    }

    matched_streams = []
    for stream_name, subjects_list in stream_mapping.items():
        for subj in selected_subjects:
            if any(subj in s or s in subj for s in subjects_list):  # partial match
                matched_streams.append(stream_name)
    matched_streams = list(set(matched_streams))  # remove duplicates
    stream = matched_streams[0] if matched_streams else "General Studies"

    # --- 2️⃣ Extracurricular mapping ---
    user_extra_level, user_extra_score = map_extracurricular_level(extracurriculars)
    user_extra = user_extra_level if user_extra_level != "none" else None
    print("RAW personality_answers from session:", session.get("personality_answers"))


    # --- 3️⃣ Personality mapping ---
    dominant_personality = get_dominant_personality(personality_answers)
    personality_categories = allowed_categories_by_personality(dominant_personality)

    # Merge personality allowed categories with matched streams
    allowed_categories = list(set([c.lower() for c in personality_categories] + [s.lower() for s in matched_streams]))

    # --- 4️⃣ Normalize subjects helper ---
    def normalize_subjects(subject_list):
        normalized = []
        for s in subject_list:
            s_clean = s.lower().replace("/", " ").replace("&", " ").replace("-", " ").strip()
            normalized.extend([x.strip() for x in s_clean.split()])
        return normalized

    normalized_selected = normalize_subjects(selected_subjects)

    print("\n=== DEBUG INFO ===")
    print("Selected Subjects:", selected_subjects)
    print("Normalized Selected Subjects:", normalized_selected)
    print("Detected Streams:", matched_streams)
    print("Merged Allowed Categories:", allowed_categories)
    print("User GPA:", gpa, "User Extra Score:", user_extra_score)
    print("Dominant Personality:", dominant_personality)

    recommended_careers = []

    extra_impact = CAREER_PATHS.get("extracurricular_impact", {})

    for category in CAREER_PATHS.get("career_categories", []):
        category_name = category.get("category", "").strip()
        if allowed_categories and category_name.lower() not in allowed_categories:
            continue

        for career in category.get("careers", []):
            required_gpa = float(career.get("required_weighted_gpa", 0))
            career_subjects = career.get("related_subjects", [])
            normalized_career_subjects = normalize_subjects(career_subjects)
            pref_extra = career.get("preferred_extracurricular", "none").lower().strip()
            career_extra_score = extra_impact.get(pref_extra, 0.0)

            if not any(word in normalized_career_subjects for word in normalized_selected):
                continue

            if gpa + user_extra_score + 0.05 < required_gpa:
                continue

            if user_extra_score + 0.02 < career_extra_score:
                continue

            recommended_careers.append({
                "name": career.get("name"),
                "category": category_name,
                "related_subjects": career.get("related_subjects", []),
                "courses": career.get("courses", []),
                "suggested_extracurriculars": career.get("suggested_extracurriculars", []),
                "preferred_extracurricular": pref_extra.capitalize()
            })

    if not recommended_careers:
        print("⚠️ No exact matches found — relaxing filters...")
        for category in CAREER_PATHS.get("career_categories", []):
            for career in category.get("careers", []):
                normalized_career_subjects = normalize_subjects(career.get("related_subjects", []))
                if any(word in normalized_career_subjects for word in normalized_selected):
                    recommended_careers.append({
                        "name": career.get("name"),
                        "category": category.get("category"),
                        "related_subjects": career.get("related_subjects", []),
                        "courses": career.get("courses", []),
                        "suggested_extracurriculars": career.get("suggested_extracurriculars", []),
                        "preferred_extracurricular": career.get("preferred_extracurricular", "none").capitalize()
                    })

    recommended_careers = recommended_careers[:6]

    session["recommendations"] = recommended_careers

    return render_template(
        "quiz/results.html",
        stream=stream,
        gpa=gpa,
        extracurriculars=extracurriculars,
        user_extra=user_extra.capitalize() if user_extra else "None",
        personality=dominant_personality,
        recommendations=recommended_careers
    )


def map_extracurricular_level(extracurriculars):
    impact_map = CAREER_PATHS.get("extracurricular_impact", {
        "none": 0.00, "basic": 0.02, "moderate": 0.05, "strong": 0.08, "exceptional": 0.10
    })

    if not extracurriculars:
        return "none", impact_map["none"]

    normalized = []
    for x in extracurriculars:
        x_clean = x.lower().replace("&", " ").replace("-", " ")
        normalized.extend(x_clean.split())

    keywords = {
        "exceptional": ["research", "innovation", "hackathon", "competition", "kaggle", "ai", "ml"],
        "strong": ["volunteering", "community", "social", "stem", "robotics", "coding", "club"],
        "moderate": ["career", "development", "arts", "music", "visual", "performing", "design", "film"],
        "basic": []
    }

    for level, words in keywords.items():
        if any(w in normalized for w in words):
            return level, impact_map[level]

    return "none", impact_map["none"]


def get_dominant_personality(personality_answers):
    trait_counts = {"Thinker": 0, "Creator": 0, "Helper": 0, "Leader": 0}

    for ans in personality_answers:
        trait = ans.get("trait") if isinstance(ans, dict) else ans
        if trait:
            trait_counts[trait] += 1

    print("Personality Count:", trait_counts)

    if not any(trait_counts.values()):
        return "Thinker"  # fallback
    return max(trait_counts, key=trait_counts.get)



# --- 3️⃣ Map allowed categories for a given personality ---
def allowed_categories_by_personality(personality):
    mapping = {
        "Thinker": ["Tech & Engineering", "Data & Analysis", "Research & Academia"],
        "Creator": ["Creative & Design", "Lifestyle & Independent Careers"],
        "Helper": ["Education & Training", "Healthcare & Wellness", "Social Impact & Nonprofit"],
        "Leader": ["Business & Entrepreneurship", "Communication & Writing"]
    }
    return mapping.get(personality, [])


@app.route("/show_career")
@login_required
def show_career():
    """Allows user to revisit their saved career recommendations from dashboard."""
    # If results were already computed
    recommendations = session.get("recommendations", [])

    # If user didn’t finish quiz yet, redirect them
    if not recommendations:
        flash("Please complete the quiz first to see your career recommendations.", "warning")
        return redirect(url_for("quizpage1"))

    selected_subjects = session.get("selected_subjects", [])
    gpa = session.get("gpa", 0)
    extracurriculars = session.get("extracurriculars", [])
    user_extra, _ = map_extracurricular_level(extracurriculars)
    personality_answers = session.get("personality_answers", [])
    dominant_personality = get_dominant_personality(personality_answers)

    return render_template(
        "quiz/results.html",
        stream="Your Stream",
        gpa=gpa,
        extracurriculars=extracurriculars,
        user_extra=user_extra.capitalize(),
        personality=dominant_personality,
        recommendations=recommendations
    )


@app.route('/dashboard')
@login_required
def dashboard():
    email = session['user']
    profile = profiles.get(email, {})
    return render_template('pages/dashboard.html', profile=profile)


@login_required
@app.route("/save_profile", methods=["POST"])
def save_profile():
    email = session["user"]  
    profiles[email] = {
        "name": request.form.get("name"),
        "grade": request.form.get("grade"),
        "gender": request.form.get("gender"),
        "location": request.form.get("location"),
        "bio": request.form.get("bio"),
        "interests": [i.strip() for i in request.form.get("interests", "").split(",") if i.strip()],
        "majors": [m.strip() for m in request.form.get("majors", "").split(",") if m.strip()],
        "skills": [s.strip() for s in request.form.get("skills", "").split(",") if s.strip()],
    }
    return redirect(url_for("dashboard"))





UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    email = session['user']  
    profile = profiles.get(email, {})  

    if request.method == 'POST':
        profile['name'] = request.form.get('name')
        profile['grade'] = request.form.get('grade')
        profile['gender'] = request.form.get('gender')
        profile['location'] = request.form.get('location')
        profile['bio'] = request.form.get('bio')
        profile['interests'] = [i.strip() for i in request.form.get('interests', '').split(',') if i.strip()]
        profile['majors'] = [m.strip() for m in request.form.get('majors', '').split(',') if m.strip()]
        profile['skills'] = [s.strip() for s in request.form.get('skills', '').split(',') if s.strip()]

        image = request.files.get('image')
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            profile['image'] = filename

        profiles[email] = profile

        return redirect(url_for('dashboard'))

    return render_template('pages/edit_profile.html', profile=profile)


if __name__ == '__main__':
    app.run(debug=True)