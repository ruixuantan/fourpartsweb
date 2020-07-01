const handleUpload = (url) => {
  console.log(url)
  const midifile = url.files[0].name
  document.getElementById("display-filename").innerHTML = midifile + " ready."
  document.getElementById("display-filename").style.backgroundColor = 'skyblue'
}

const handleSubmit = (event) => {

  let midifile = document.getElementById("midi-input").files[0]; 
  console.log(midifile)

  if (midifile == null) {
    alert("Upload a file first!")
    return null
  }

  const formData = new FormData()
  formData.append('file', midifile)

  const uploadData = {
    method: 'POST',
    body: formData
  }

  fetch('/api/v1/midifile/', uploadData)
    .then(res => {
      if (res.status !== 200) {
        console.log(res.status)
      }
      return res.json()
    })
    .then(responseData => {
      if (responseData.hasOwnProperty('error')) {
        alert(responseData.error)
        document.getElementById("display-filename").innerHTML = 'An error occured'
        document.getElementById("display-filename").style.backgroundColor = 'red'
      } else {
        location.href = '/download/' + responseData
        document.getElementById("display-filename").innerHTML = 'Success!'
        document.getElementById("display-filename").style.backgroundColor = '#4baf50'
      }
      midifile = null
      document.getElementById("midi-input").value = null
    })
    .catch(err => {
      console.log(err)
    })
}
