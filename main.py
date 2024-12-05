import streamlit as st

# Streamlit App Title
st.title("Power BI Dashboard")

# Embed Power BI Report with Full-Screen Support
st.components.v1.html(
    """
    <div style="position: relative; height: 0; overflow: hidden; padding-bottom: 56.25%;">
        <iframe 
            id="powerbi-frame"
            src="https://app.powerbi.com/reportEmbed?reportId=e8fee0b6-c10f-468b-a03a-ec39d373e420&autoAuth=true&ctid=a5d4252a-02f9-4e60-96f0-9733baae4919" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    </div>
    <button onclick="openFullScreen()">Go Full Screen</button>

    <script>
    function openFullScreen() {
        var iframe = document.getElementById("powerbi-frame");
        if (iframe.requestFullscreen) {
            iframe.requestFullscreen();
        } else if (iframe.mozRequestFullScreen) { /* Firefox */
            iframe.mozRequestFullScreen();
        } else if (iframe.webkitRequestFullscreen) { /* Chrome, Safari, Opera */
            iframe.webkitRequestFullscreen();
        } else if (iframe.msRequestFullscreen) { /* IE/Edge */
            iframe.msRequestFullscreen();
        }
    }
    </script>
    """,
    height=600,  # Adjust iframe height
)
