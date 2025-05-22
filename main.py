import streamlit as st

# --- Functions ---

# Append new todo
def append_todo(todos, new_todo):
    if new_todo:
        todos.append(new_todo)
    return todos

# Delete todo by index
def delete_todo(index):
    todos = st.session_state["todos"]
    todos.pop(index)
    st.session_state["todos"] = todos
    st.session_state["edit_index"] = -1
    st.experimental_rerun()  # Refresh app immediately

# Update todo by index
def update_todo(index, new_value):
    todos = st.session_state["todos"]
    todos[index] = new_value
    st.session_state["todos"] = todos

# Add todo handler
def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo.strip() != "":
        st.session_state["todos"] = append_todo(st.session_state["todos"], new_todo.strip())
    st.session_state["new_todo"] = ""  # Clear input field


# --- App Setup ---

# Initialize session state variables
if "todos" not in st.session_state:
    st.session_state["todos"] = []

if "edit_index" not in st.session_state:
    st.session_state["edit_index"] = -1

# --- UI ---

st.title("✅ My Todo App")
st.subheader("This app will increase my productivity 💪")

# Display todos
for i, todo in enumerate(st.session_state["todos"]):
    col1, col2, col3 = st.columns([6, 1, 1])

    # If in edit mode
    if st.session_state["edit_index"] == i:
        new_todo_text = col1.text_input("Edit todo", value=todo, key=f"edit_todo_{i}")
        if col2.button("💾 Save", key=f"save_{i}"):
            update_todo(i, new_todo_text)
            st.session_state["edit_index"] = -1
        if col3.button("❌ Cancel", key=f"cancel_{i}"):
            st.session_state["edit_index"] = -1
    else:
        col1.checkbox(todo, key=f"todo_{i}", disabled=True)
        if col2.button("✏️ Edit", key=f"edit_{i}"):
            st.session_state["edit_index"] = i
        if col3.button("🗑️ Delete", key=f"delete_{i}"):
            delete_todo(i)

# Add new todo input
st.text_input(
    label="➕ Enter your todo",
    placeholder="Add your todo",
    on_change=add_todo,
    key='new_todo'
)
