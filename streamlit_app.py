# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# JavaScript code to handle form submission
javascript_code = """
<script>
function submitForm() {
    var form = document.getElementById("myForm");
    var submissionMessage = document.getElementById("submissionMessage");

    // Display "Submitting..." message
    submissionMessage.innerHTML = "Submitting...";

    // Submit the form asynchronously
    fetch(form.action, {
        method: form.method,
        body: new FormData(form)
    }).then(function(response) {
        // Handle response here, e.g., display success message
        submissionMessage.innerHTML = "Form submitted successfully!";
        form.reset(); // Optional: Reset the form after successful submission
    }).catch(function(error) {
        // Handle errors here, e.g., display error message
        submissionMessage.innerHTML = "Error submitting form: " + error.message;
    });

    return false; // Prevent the default form submission
}
</script>
"""

# Display the JavaScript code using Streamlit
st.markdown(javascript_code, unsafe_allow_html=True)


