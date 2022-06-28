function deleteNote(noteId) {
    fetch('deleteN-note', {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),

        }).then((_res) =>{

    window.location.href= "/";
    });
}