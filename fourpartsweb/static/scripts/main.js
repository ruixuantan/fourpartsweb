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
  }
}

const fileInput = () => {
  $("#midi-input").change((event) => {
    const midifile = event.target.files[0].name
    console.log(midifile)
    statusBar(midifile, "READY")
  })
}

const fileUpload = () => {

  $("button").click(() => {

    let midifile = $("#midi-input")[0].files[0]
    const formData = new FormData()
    formData.append('file', midifile)

    if (midifile == null) {
      alert("Upload a file first!")
      return null
    }

    $.ajax({
      url: '/api/v1/midifile/',
      type: 'post',
      data: formData,
      contentType: false,
      processData: false,
      success: (res) => {
        console.log(res)
        location.href = '/download/' + res
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

$(document).ready(() => {
  fileInput()
  fileUpload()
})
