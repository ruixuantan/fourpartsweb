const statusBar = (msg, selector) => {
  if (selector === "READY") {
    $("#status-bar").text(msg + " ready.")
    $("#status-bar").css("background-color", "skyblue")

  } else if (selector === "FAIL") {
    $("#status-bar").text("An error occured")
    $("#status-bar").css("background-color", "red")

  } else if (selector === "SUCCESS") {
    $("#status-bar").text("Success!")
    $("#status-bar").css("background-color", "#4baf50")

  } else if (selector === "CLEAR") {
    $("#status-bar").text("")
    $("#status-bar").css("background-color", "white")
  }
}


const fileInput = () => {
  $("#midi-input").change((event) => {
    const midifile = event.target.files[0].name
    console.log(midifile)

    if (midifile.substr(midifile.length - 4) !== ".mid") {
      alert("Please upload .mid files only")
      $("#midi-input").val(null)
      statusBar("", "CLEAR")
    } else {
      statusBar(midifile, "READY")
    }
  })
}


const downloadFile = (data, type, filename) => {
  const blob = new Blob([data], { type: type })
  const link = document.createElement('a')

  link.href = window.URL.createObjectURL(blob)
  link.download = filename

  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}


const fileUpload = () => {

  $(".file-upload-btn").click(() => {

    let midifile = $("#midi-input")[0].files[0]
    const formData = new FormData()
    formData.append('file', midifile)

    if (midifile == null) {
      alert("Upload a file first!")
      statusBar("", "CLEAR")
      return null
    }

    $.ajax({
      url: '/api/v1/midifile/',
      type: 'post',
      data: formData,
      contentType: false,
      processData: false,
      async: false,
      success: (data, textStatus, jqXHR) => {
        downloadFile(data, 
                     jqXHR.getResponseHeader('content-type'), 
                     midifile.name.slice(0, -4) + ".csv")
        statusBar("", "SUCCESS")
      },
      error: (err) => {
        console.log(err)
        statusBar("", "FAIL")
      }
    })

    midifile = null
    $("#midi-input").val(null)
  })
}


const downloadStorage = () => {
  $("#download-storage").click(() => {

    const key = $("#download-key").val()
    const data = {key: key}
    console.log(data)

    $.ajax({
      url: '/api/v1/download/',
      type: 'post',
      data: JSON.stringify(data),
      contentType: 'application/json',
      processData: false,
      success: (data, textStatus, jqXHR) => {
        console.log(this.response)
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR.getResponseHeader('content-disposition'))

        const type = jqXHR.getResponseHeader('content-type')
        console.log(type)

        downloadFile(data, type, "storage.zip")

        $("#download-status").text("Download completed.")
      },
      error: (data, textStatus, jqXHR) => {
        console.log(data.getAllResponseHeaders())
        console.log(textStatus)
        console.log(jqXHR)
        $("#download-status").text("Please check key entered.")
      }
    })
  })
}


$(document).ready(() => {
  fileInput()
  fileUpload()
  downloadStorage()
})
