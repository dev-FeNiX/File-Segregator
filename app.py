import streamlit as st
from organizer import organize_files
import time

st.set_page_config(page_title="File Organizer", page_icon="📁", layout="centered")

st.title("📁 File Organizer")
st.markdown("Organize your files by type into folders with one click.")

folder = st.text_input("Enter folder path to organize", value="")

if st.button("Organize Files"):
    if not folder:
        st.error("Please enter a valid folder path!")
    else:
        try:
            progress_text = st.empty()
            progress_bar = st.progress(0)

            def progress_cb(current, total):
                progress_text.text(f"Moving file {current} of {total}...")
                progress_bar.progress(current / total)

            moved = organize_files(folder, progress_callback=progress_cb)

            st.success(f"✅ Successfully moved {moved} files.")
        except FileNotFoundError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
