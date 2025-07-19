import streamlit as st

# --- Define courses based on level and department ---

General_Phy_level1={
    "English Language for Science [Uni1101]":2,
    'Introduction  to Computer  Science [Com1101]':2,
    "General Mathematics  I (Calculus I) [Mat1101]":2,
    "General Mathematics  II (Introduction to Algebra) [Mat1103]":2,
    "General Physics I [Phy1101]":2,
    "Practical Physics I [Phy1103]":1,
    "General Chemistry I [Chm1101]":2,
    "Practical Chemistry I [Chm1103]":1,
    "Principals of Zoolgy [Zoo1103]":2,
    "Information  Technology [Uni1202]":2,
    "Introduction  to Programming [Com1202]":2,
    "General Mathematics III  (Calculus II) [Mat1202]":2,
    "General Mathematics  IV (Mechanics I) [Mat1204]":2,
    "General Physics II [Phy1202]":2,
    "Practical Physics II [Phy1204]":1,
    "General Chemistry II [Chm1202]":2,
    "Practical Chemistry II [Chm1204]":1,
    "Introduction to  Botany [Bot1103]":2

}

General_Bio_level1={
    "English Language for Science [Uni1101]":2,
    "General Botany I [Bot1101]":3,
    "General Zoology I [Zoo1101]":3,
    "General Chemistry I [Chm1101]":2,
    "Practical Chemistry I [Chm1103]":1,
    "Physics for Biology I [Phy1105]":2,
    "General Mathematics I (Calculus I) [Mat1101]":2,
    "Introduction to  Statistics [Sta1208]":1,
    "Information  Technology [Uni1202]":2,
    "General Botany II [Bot1202]":3,
    "General Zoology II [Zoo1202]":3,
    "General Chemistry II [Chm1202]":2,
    "Practical Chemistry II [Chm1204]":1,
    "Physics  for Biology II [Phy1206]":2,
    "IntrIoducion  to Computer Science [Com1101]":2,
    "Practical Computer Science [Com1103]":1
}

General_Geo_level1={
    "English Language for Science [Uni1101]":2,
    "General Geology I [Geo1101]":2,
    "General  Mathematics I  (Calculus I) [Mat1101]":2,
    "Introduction to  Statistics [Sta 1208]":1,
    "General Physics I [Phy1101]":2,
    "Practical Physics I [Phy1103]":1,
    "General Chemistry  I [Chm1101]":2,
    "Practical General Chemistry I [Chm1103]":1,
    "Introduction of Zoolgy [Zoo1103]":2,
    "Information  Technology [Uni1202]":2,
    "General Geophysics [GPh1202]":2,
    "General Geology II [Geo1202]":2,
    "Introduction  to Computer  Science [Com1101]":2,
    "Practical Computer Science [Com1103]":1,
    "General Physics II [Phy1202]":2,
    "Practical Physics  II [Phy1204]":1,
    "General Chemistry II [Chm1202]":2,
    "Practical General Chemistry II [Chm1204]":1,
    "Introduction to Botany [Bot1103]":2
}
COURSES_BY_LEVEL_AND_DEPARTMENT = {
    1: {
        "العلوم الطبيعية": (list(General_Phy_level1.keys())),
        "علوم الأرض": list(General_Geo_level1.keys()),
        "العلوم البيولوجية": list(General_Bio_level1.keys())

    },
    2: {
        "الرياضيات": ["Intermediate Python", "Computer Networks"],
        "الرياضيات وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الاحصاء وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الفيزياء": ["Business Communication", "Intro to Economics"],
        "الفيزياء الحيوية الطبية": ["Business Communication", "Intro to Economics"],
        "علوم الفضاء": ["Business Communication", "Intro to Economics"],
        "الكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء التطبيقية": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا": ["Business Communication", "Intro to Economics"],
        "الجيوفيزياء": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا والكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "النبات": ["Business Communication", "Intro to Economics"],
        "النبات والكيمياء": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي والكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "علم الحيوان": ["Business Communication", "Intro to Economics"],
        "علم الحيوان والكيمياء": ["Business Communication", "Intro to Economics"],
        "التكنولوجيا الحيوية الجزئية": ["Business Communication", "Intro to Economics"],

    },
    3: {
        "الرياضيات": ["Intermediate Python", "Computer Networks"],
        "الرياضيات وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الاحصاء وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الفيزياء": ["Business Communication", "Intro to Economics"],
        "الفيزياء الحيوية الطبية": ["Business Communication", "Intro to Economics"],
        "علوم الفضاء": ["Business Communication", "Intro to Economics"],
        "الكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء التطبيقية": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا": ["Business Communication", "Intro to Economics"],
        "الجيوفيزياء": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا والكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "النبات": ["Business Communication", "Intro to Economics"],
        "النبات والكيمياء": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي والكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "علم الحيوان": ["Business Communication", "Intro to Economics"],
        "علم الحيوان والكيمياء": ["Business Communication", "Intro to Economics"],
        "التكنولوجيا الحيوية الجزئية": ["Business Communication", "Intro to Economics"],

    },
    4: {
        "الرياضيات": ["Intermediate Python", "Computer Networks"],
        "الرياضيات وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الاحصاء وعلوم الحاسب": ["Business Communication", "Intro to Economics"],
        "الفيزياء": ["Business Communication", "Intro to Economics"],
        "الفيزياء الحيوية الطبية": ["Business Communication", "Intro to Economics"],
        "علوم الفضاء": ["Business Communication", "Intro to Economics"],
        "الكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء التطبيقية": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا": ["Business Communication", "Intro to Economics"],
        "الجيوفيزياء": ["Business Communication", "Intro to Economics"],
        "الجيولوجيا والكيمياء": ["Business Communication", "Intro to Economics"],
        "الكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "النبات": ["Business Communication", "Intro to Economics"],
        "النبات والكيمياء": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي": ["Business Communication", "Intro to Economics"],
        "الميكروبيولوجي والكيمياء الحيوية": ["Business Communication", "Intro to Economics"],
        "علم الحيوان": ["Business Communication", "Intro to Economics"],
        "علم الحيوان والكيمياء": ["Business Communication", "Intro to Economics"],
        "التكنولوجيا الحيوية الجزئية": ["Business Communication", "Intro to Economics"],

    }
}

# --- UI ---
st.title("🌞 Summer Course Planner")

name = st.text_input("Enter your name:")
code = st.text_input("Enter your code:")
level = st.selectbox("Select your level:", list(COURSES_BY_LEVEL_AND_DEPARTMENT.keys()))
hours = st.number_input("Enter total hours achieved:", min_value=0, step=1)

if name and code and hours:
    st.markdown("---")
    st.subheader("🎓 Department & Course Selection")

    departments = list(COURSES_BY_LEVEL_AND_DEPARTMENT[level].keys())
    department = st.selectbox("Select your department:", departments)

    # Show courses for selected level and department
    if department:
        available_courses = COURSES_BY_LEVEL_AND_DEPARTMENT[level][department]
        selected_courses = st.multiselect("Select your summer courses:", available_courses)

        if selected_courses:
            st.markdown("### ✅ Selected Courses:")
            for i, course in enumerate(selected_courses, 1):
                st.write(f"{i}. {course}")
        else:
            st.info("Please select at least one course.")
