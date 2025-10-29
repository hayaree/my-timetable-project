import streamlit as st
import pandas as pd
import random # ไลบรารีสำหรับ "สุ่ม"

# --- 1. ข้อมูลตัวอย่าง (Input) ---
# (ในชีวิตจริง ข้อมูลนี้จะเยอะกว่านี้)
teachers = ["ครู ก", "ครู ข"]
subjects = ["คณิต", "วิทย์", "อังกฤษ", "พละ"]
rooms = ["ห้อง 101", "ห้อง 102", "สนาม"]
times = ["จันทร์-เช้า", "จันทร์-บ่าย", "อังคาร-เช้า", "อังคาร-บ่าย"]
groups = ["กลุ่ม 1 (ปวส.)", "กลุ่ม 2 (ปวส.)"]

# --- 2. หน้าตาเว็บแอป (Streamlit) ---
st.title("ระบบจัดตารางสอนอัตโนมัติ (v1 - แบบสุ่ม)")
st.write("เวอร์ชันนี้เป็นแค่การสุ่มมั่วๆ เพื่อทดสอบระบบ")

if st.button("ลองจัดตารางแบบสุ่ม!"):

    # --- 3. ตรรกะแบบง่าย (Heuristic) ---
    # "สุ่ม" ตารางสอนสำหรับแต่ละกลุ่มเรียน

    final_schedule = []

    for group in groups:
        for time in times:
            # สุ่มวิชา, ครู, และห้อง
            random_subject = random.choice(subjects)
            random_teacher = random.choice(teachers)
            random_room = random.choice(rooms)

            # เพิ่มลงในตารางผลลัพธ์
            final_schedule.append({
                "กลุ่มเรียน": group,
                "เวลา": time,
                "วิชา": random_subject,
                "ครู": random_teacher,
                "ห้อง": random_room
            })

    # --- 4. แสดงผลลัพธ์ (Output) ---
    st.subheader("ผลลัพธ์ตารางสอน (แบบสุ่ม)")

    # แปลงเป็นตารางสวยๆ ด้วย Pandas
    df = pd.DataFrame(final_schedule)
    st.dataframe(df)

    st.warning("หมายเหตุ: ตารางนี้อาจมีข้อผิดพลาด (ครูซ้อน/ห้องซ้อน) เพราะยังไม่ได้ใช้ AI")