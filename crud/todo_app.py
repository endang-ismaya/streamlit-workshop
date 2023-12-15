import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

import sys
from os import getcwd
from os.path import join, dirname, normpath, realpath, expanduser


# Package parent
PACKAGE_PARENT = "../"
SCRIPT_DIR = dirname(realpath(join(getcwd(), expanduser(__file__))))
sys.path.append(normpath(join(SCRIPT_DIR, PACKAGE_PARENT)))

# utils
from utils.toget import ExclusiveEnum  # noqa: E402
from crud.db_conn import (  # noqa: E402
    create_table,
    add_todo,
    view_all_data,
    view_unique_todo,
    get_todo,
    update_todo,
    delete_todo,
)


def convert_string_to_date(date_string):
    try:
        # Parse the string date using datetime.strptime
        datetime_obj = datetime.strptime(date_string, "%Y-%m-%d")

        # Extract the date part
        date_obj = datetime_obj.date()

        return date_obj

    except ValueError as e:
        # Handle the case where the input string is not in the expected format
        print(f"Error: {e}")
        return None


class TodoStatus(ExclusiveEnum):
    Todo = "Todo"
    InProgress = "InProgress"
    Done = "Done"


def create_page():
    st.subheader("Add Todo")

    # layout
    col1, col2 = st.columns(spec=2)

    with col1:
        todo = st.text_area("Task To Do", height=150)

    with col2:
        todo_status = st.selectbox("Status", TodoStatus.list())
        todo_due = st.date_input("Due Date")

    btn_add = st.button("Add Todo", type="primary")

    if btn_add:
        with st.spinner("adding todo..."):
            add_todo(todo=todo, todo_status=todo_status, todo_due=todo_due)
        st.success("New Todo has been added successfully.")

    # view data
    st.divider()
    with st.expander("View All Data"):
        datas = view_all_data()

        df = pd.DataFrame(datas, columns=["Id", "ToDo", "Status", "Due Date"])
        st.dataframe(df)
        # st.write(datas)

        task_df = df["Status"].value_counts().to_frame()
        task_df = task_df.reset_index()

        # table count
        st.dataframe(task_df)

        # chart
        p1 = px.pie(task_df, names="Status", values="count")
        st.plotly_chart(p1)


def get_all_data():
    datas = view_all_data()
    df = pd.DataFrame(datas, columns=["Id", "ToDo", "Status", "Due Date"])

    return df


def update_page():
    st.subheader("Update Todo")

    table_view = st.empty()
    table_view.dataframe(get_all_data(), hide_index=True)

    # l_todos = [i[0] for i in view_unique_todo()]
    todo_data = view_unique_todo()
    selected_todo = st.selectbox(
        "Select ToDo To Update/Delete",
        todo_data,
    )
    selected_result = get_todo(selected_todo[0])

    if selected_result:
        is_updated = None
        is_deleted = None

        todo = selected_result[0][1]
        todo_status = selected_result[0][2]
        todo_due = selected_result[0][3]  # 2023-12-17
        todo_date = convert_string_to_date(todo_due)
        todo_id = selected_result[0][0]

        # layout
        col1, col2 = st.columns(spec=2)

        with col1:
            todo_ui = st.text_area("ToDo", height=150, value=todo)

        with col2:
            idx = TodoStatus.list().index(todo_status)
            todo_status_ui = st.selectbox("Status", TodoStatus.list(), index=idx)
            todo_due_ui = st.date_input("Due Date", todo_date)

        col_update, col_delete = st.columns(spec=2)

        with col_update:
            btn_update = st.button("Update Todo", type="primary")

            if btn_update:
                with st.spinner("updating data..."):
                    is_updated = update_todo(
                        todo_id, todo_ui, todo_status_ui, todo_due_ui
                    )
                    table_view.dataframe(get_all_data(), hide_index=True)

        if is_updated:
            st.success(f"'{todo}' has been updated successfully.")

        with col_delete:
            btn_delete = st.button("Delete Todo", type="secondary")

            if btn_delete:
                with st.spinner("deleting data..."):
                    is_deleted = delete_todo(todo_id=todo_id)
                    table_view.dataframe(get_all_data(), hide_index=True)

        if is_deleted:
            st.warning(f"'{todo}' has been deleted successfully.")


def main():
    """main point"""
    st.title("Todo App with Streamlit")

    menu = ["Add ToDo", "Update Todo"]
    choice = st.sidebar.selectbox("Navigation", menu)

    # create db
    create_table()

    match choice:
        case "Add ToDo":
            create_page()

        case "Update Todo":
            update_page()
        case _:
            raise NotImplementedError("Wrong Page")


if __name__ == "__main__":
    main()
