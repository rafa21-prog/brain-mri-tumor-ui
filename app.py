
import streamlit as st

st.set_page_config(
    page_title="Brain MRI Tumor Classification",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Brain MRI Tumor Classification")
st.write("### DenseNet121 + SVM Based Classification")
st.write(
    "Upload a brain MRI image to explore the tumor "
    "classification system."
)

uploaded_file = st.file_uploader(
    "Upload Brain MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(
        uploaded_file,
        caption="Uploaded Brain MRI Image",
        use_container_width=True
    )

    st.info(
        "Image uploaded successfully. "
        "Model prediction will be added in the next step."
    )

st.caption(
    "Academic thesis demonstration only — "
    "not intended for medical diagnosis."
)
