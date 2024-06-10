function deleteNote(noteId) {
  fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Failed to delete note');
      }
      return response.json();
  })
  .then(data => {
      // Optional: Handle success response, e.g., show a message or update UI
      console.log(data.message);
      // Redirect to the note page after successful deletion
      window.location.href = "/note"; // Assuming the note page URL is "/note"
  })
  .catch(error => {
      console.error('Error:', error);
      // Optional: Handle error, e.g., show an error message to the user
  });
}

