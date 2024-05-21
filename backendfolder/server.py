import os
import base64
import dash
from dash import dcc, html, Input, Output, State
from flask import Flask
from pydub import AudioSegment
from transcribe_function import transcribe_audio

# Define the upload folder
UPLOAD_FOLDER_ROOT = "uploads"
if not os.path.exists(UPLOAD_FOLDER_ROOT):
    os.makedirs(UPLOAD_FOLDER_ROOT)


# Initialize Flask server
server = Flask(__name__)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_ROOT

# Initialize Dash app
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("test server"),
    dcc.Upload(
        id='upload-audio',
        children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    html.Button('Transcribe', id='transcribe-button', n_clicks=0, disabled=True),
    html.Div(id='output-transcription', style={'whiteSpace': 'pre-line'}),
    html.Div(id='upload-status', style={'color': 'red'}),
    html.Div(id='debug-info', style={'color': 'blue'})
])

@app.callback(
    [Output('transcribe-button', 'disabled'),
     Output('upload-status', 'children'),
     Output('debug-info', 'children')],
    [Input('upload-audio', 'contents')],
    [State('upload-audio', 'filename')],
    prevent_initial_call=True
)
def enable_transcribe_button(contents, filename):
    if contents:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        file_path = os.path.join(UPLOAD_FOLDER_ROOT, filename)
        with open(file_path, "wb") as f:
            f.write(decoded)
        debug_info = f"Upload Path: {file_path}"
        if os.path.exists(file_path):
            return False, f"File {filename} uploaded successfully.", debug_info
        else:
            return True, f"File upload failed: {filename} not found in {UPLOAD_FOLDER_ROOT}.", debug_info
    return True, "", ""

@app.callback(
    Output('output-transcription', 'children'),
    Input('transcribe-button', 'n_clicks'),
    State('upload-audio', 'filename'),
    prevent_initial_call=True
)
def update_output(n_clicks, filename):
    if n_clicks > 0 and filename:
        audio_path = os.path.join(UPLOAD_FOLDER_ROOT, filename)
        if os.path.exists(audio_path):
            # Convert audio to WAV format if necessary
            if not audio_path.endswith(".wav"):
                audio = AudioSegment.from_file(audio_path)
                audio_path_wav = os.path.join(UPLOAD_FOLDER_ROOT, f"{os.path.splitext(filename)[0]}.wav")
                audio.export(audio_path_wav, format="wav")
                audio_path = audio_path_wav

            transcription = transcribe_audio(audio_path)
            return transcription
        else:
            return f"File not found: {audio_path}"
    return "Please upload an audio file."

if __name__ == '__main__':
    app.run_server(debug=True)








