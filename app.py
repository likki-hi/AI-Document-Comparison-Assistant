
import streamlit as st
import pandas as pd

from io import BytesIO
from xml.sax.saxutils import escape

from document_reader import extract_text, get_keywords
from semantic_comparison import calculate_semantic_similarity

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AI Document Comparison Assistant",
    page_icon="📄",
    layout="wide"
)


# --------------------------------
# PDF REPORT GENERATION
# --------------------------------

def create_pdf_report(
    doc1_name,
    doc2_name,
    keyword_similarity,
    semantic_similarity,
    only_in_doc1,
    only_in_doc2,
    common_keywords
):
    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph("AI Document Comparison Report", styles["Title"])
    )
    story.append(Spacer(1, 18))

    story.append(Paragraph("Documents Compared", styles["Heading2"]))
    story.append(
        Paragraph("Document 1: " + escape(doc1_name), styles["Normal"])
    )
    story.append(
        Paragraph("Document 2: " + escape(doc2_name), styles["Normal"])
    )
    story.append(Spacer(1, 18))

    story.append(Paragraph("Similarity Results", styles["Heading2"]))

    table_data = [
        ["Metric", "Similarity"],
        ["Keyword Similarity", f"{keyword_similarity:.2f}%"],
        ["Semantic Similarity", f"{semantic_similarity:.2f}%"]
    ]

    results_table = Table(table_data, colWidths=[250, 150])
    results_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP")
    ]))

    story.append(results_table)
    story.append(Spacer(1, 18))

    def add_keyword_section(title, words):
        story.append(Paragraph(title, styles["Heading2"]))

        if words:
            safe_words = ", ".join(
                escape(str(word)) for word in sorted(words)
            )
            story.append(Paragraph(safe_words, styles["Normal"]))
        else:
            story.append(
                Paragraph("No keywords found.", styles["Normal"])
            )

        story.append(Spacer(1, 12))

    add_keyword_section("Common Keywords", common_keywords)
    add_keyword_section("Keywords Only in Document 1", only_in_doc1)
    add_keyword_section("Keywords Only in Document 2", only_in_doc2)

    story.append(Spacer(1, 10))
    story.append(
        Paragraph(
            "Note: Keyword similarity measures shared unique words. "
            "Semantic similarity estimates similarity in meaning and "
            "does not prove the documents are equivalent.",
            styles["Italic"]
        )
    )

    pdf.build(story)
    buffer.seek(0)

    return buffer.getvalue()


# --------------------------------
# MAIN APPLICATION
# --------------------------------

st.title("📄 AI Document Comparison Assistant")

st.write(
    "Upload two PDF documents to compare their keywords and meanings, "
    "view similarity scores, and download a comparison report."
)

st.divider()


# --------------------------------
# UPLOAD DOCUMENTS
# --------------------------------

col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader(
        "📁 Upload First PDF",
        type=["pdf"],
        key="document1"
    )

with col2:
    file2 = st.file_uploader(
        "📁 Upload Second PDF",
        type=["pdf"],
        key="document2"
    )


# --------------------------------
# EXTRACT AND COMPARE DOCUMENTS
# --------------------------------

if file1 is not None and file2 is not None:

    st.success("Both PDF documents were uploaded successfully!")

    try:
        text1 = extract_text(file1)
        text2 = extract_text(file2)

        st.subheader("📖 Extracted Document Text")

        with st.expander(f"Document 1: {file1.name}"):
            if text1 and text1.strip():
                st.text_area(
                    "First document content",
                    value=text1,
                    height=250,
                    disabled=True,
                    key="text1_preview"
                )
            else:
                st.warning(
                    "No text was extracted from the first PDF. "
                    "It may be scanned or image-based."
                )

        with st.expander(f"Document 2: {file2.name}"):
            if text2 and text2.strip():
                st.text_area(
                    "Second document content",
                    value=text2,
                    height=250,
                    disabled=True,
                    key="text2_preview"
                )
            else:
                st.warning(
                    "No text was extracted from the second PDF. "
                    "It may be scanned or image-based."
                )

        st.divider()

        if st.button(
            "🔍 Compare Documents",
            type="primary",
            use_container_width=True
        ):

            if not text1 or not text1.strip():
                st.error("Could not extract text from the first PDF.")

            elif not text2 or not text2.strip():
                st.error("Could not extract text from the second PDF.")

            else:
                with st.spinner("Comparing documents..."):

                    # Get keywords
                    keywords1 = set(get_keywords(text1))
                    keywords2 = set(get_keywords(text2))

                    # Find common and unique keywords
                    common_keywords = keywords1 & keywords2
                    only_in_doc1 = keywords1 - keywords2
                    only_in_doc2 = keywords2 - keywords1

                    # Calculate keyword similarity
                    all_keywords = keywords1 | keywords2

                    if all_keywords:
                        keyword_similarity = (
                            len(common_keywords) / len(all_keywords)
                        ) * 100
                    else:
                        keyword_similarity = 0.0

                    # Calculate semantic similarity
                    semantic_similarity = (
                        calculate_semantic_similarity(text1, text2)
                    )

                st.success("Document comparison completed!")

                # --------------------------------
                # DISPLAY RESULTS
                # --------------------------------

                st.subheader("📊 Comparison Results")

                metric1, metric2 = st.columns(2)

                with metric1:
                    st.metric(
                        "Keyword Similarity",
                        f"{keyword_similarity:.2f}%"
                    )

                with metric2:
                    st.metric(
                        "Semantic Similarity",
                        f"{semantic_similarity:.2f}%"
                    )

                # --------------------------------
                # SIMILARITY CHART
                # --------------------------------

                st.subheader("📈 Similarity Comparison Chart")

                chart_data = pd.DataFrame({
                    "Comparison Type": [
                        "Keyword Similarity",
                        "Semantic Similarity"
                    ],
                    "Similarity (%)": [
                        keyword_similarity,
                        semantic_similarity
                    ]
                })

                # Compatible with Streamlit versions
                # that do not support y_min and y_max.
                st.bar_chart(
                    chart_data,
                    x="Comparison Type",
                    y="Similarity (%)"
                )

                # --------------------------------
                # KEYWORD STATISTICS
                # --------------------------------

                st.subheader("🔢 Keyword Statistics")

                stat1, stat2, stat3 = st.columns(3)

                with stat1:
                    st.metric(
                        "Document 1 Unique Keywords",
                        len(keywords1)
                    )

                with stat2:
                    st.metric(
                        "Document 2 Unique Keywords",
                        len(keywords2)
                    )

                with stat3:
                    st.metric(
                        "Common Keywords",
                        len(common_keywords)
                    )

                # --------------------------------
                # DISPLAY KEYWORDS
                # --------------------------------

                st.divider()

                with st.expander("📄 Keywords Only in Document 1"):
                    if only_in_doc1:
                        st.write(", ".join(sorted(only_in_doc1)))
                    else:
                        st.write("No unique keywords found.")

                with st.expander("📄 Keywords Only in Document 2"):
                    if only_in_doc2:
                        st.write(", ".join(sorted(only_in_doc2)))
                    else:
                        st.write("No unique keywords found.")

                with st.expander("🤝 Common Keywords"):
                    if common_keywords:
                        st.write(", ".join(sorted(common_keywords)))
                    else:
                        st.write("No common keywords found.")

                # --------------------------------
                # DOWNLOAD PDF REPORT
                # --------------------------------

                st.divider()
                st.subheader("📥 Download Comparison Report")

                try:
                    report = create_pdf_report(
                        file1.name,
                        file2.name,
                        keyword_similarity,
                        semantic_similarity,
                        only_in_doc1,
                        only_in_doc2,
                        common_keywords
                    )

                    st.download_button(
                        label="📄 Download Comparison Report (PDF)",
                        data=report,
                        file_name="document_comparison_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )

                except Exception as error:
                    st.error(
                        f"Could not generate the PDF report: {error}"
                    )

                st.caption(
                    "Keyword similarity measures shared unique words. "
                    "Semantic similarity estimates similarity in meaning; "
                    "it does not prove the documents are equivalent."
                )

    except Exception as error:
        st.error(
            f"An error occurred while processing the PDFs: {error}"
        )

else:
    st.info("Please upload two PDF documents to begin.")
