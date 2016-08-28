$(document).ready(function(){
    var editor = CodeMirror.fromTextArea(document.getElementById("codemirror-textarea"), {
        mode: {name: 'python',
               version: 3,
               singleLineStringErrors: false},
        lineNumbers: true,
        indentUnit: 4,
        theme: "dracula",
        matchBrackets: true
    });
});