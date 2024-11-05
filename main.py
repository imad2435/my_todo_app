import streamlit as st


def append_todo(todos, new_todo):
    if new_todo:
        todos.append(new_todo)
    return todos

if "todos" not in st.session_state:
    st.session_state["todos"] = []


def add_todo():
    # Append the new to-do to the session state list
    new_todo = st.session_state["new_todo"]
    st.session_state["todos"] = append_todo(st.session_state["todos"], new_todo)
    # Clear the input field
    st.session_state["new_todo"] = ""

st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app will increase my productivity")

for todo in st.session_state["todos"]:
    st.checkbox(todo)

# Checkboxes for the todo items
st.checkbox("Buy tomato")
st.checkbox("banana")
st.checkbox("potato")
# Text input for adding new todos
st.text_input(label="Enter your todo", placeholder="add your todo",
              on_change=add_todo, key='new_todo')
