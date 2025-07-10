import streamlit as st

st.title("📝 Simple To-Do List")

# Initialize task list
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
new_task = st.text_input("Add a task")
if st.button("Add Task") and new_task:
    st.session_state.tasks.append({"task": new_task, "completed": False})

# Show tasks
st.write("### Your Tasks")
for i, t in enumerate(st.session_state.tasks):
    completed = st.checkbox(t["task"], value=t["completed"], key=i)
    st.session_state.tasks[i]["completed"] = completed

# Clear completed tasks
if st.button("Clear Completed"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["completed"]]

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []
