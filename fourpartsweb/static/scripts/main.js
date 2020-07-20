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

  const clearMidi = () => {
    midifile = null
    $("#midi-input").val(null)
  }

  $(".file-upload-btn").click(() => {

    let midifile = $("#midi-input")[0].files[0]
    const formData = new FormData()
    formData.append('file', midifile)

    if (midifile == null) {
      alert("Upload a file first!")
      statusBar("", "CLEAR")
      return null
    }

    return $.ajax({
      url: '/api/v1/midifile/',
      type: 'post',
      data: formData,
      contentType: false,
      processData: false,
      success: (data, textStatus, jqXHR) => {
        downloadFile(data, 
                     jqXHR.getResponseHeader("content-type"), 
                     midifile.name.slice(0, -4) + ".csv")
        statusBar("", "SUCCESS")
        clearMidi()
      },
      error: (err) => {
        console.log(err)
        statusBar("", "FAIL")
        clearMidi()
      }
    })
  })
}


const ajaxConfig = () => {
  $.ajaxTransport("+binary", function (options, originalOptions, jqXHR) {
    // check for conditions and support for blob / arraybuffer response type
    if (window.FormData && ((options.dataType && (options.dataType == 'binary')) || (options.data && ((window.ArrayBuffer && options.data instanceof ArrayBuffer) || (window.Blob && options.data instanceof Blob))))) {
      return {
        // create new XMLHttpRequest
        send: function (headers, callback) {
          // setup all variables
          var xhr = new XMLHttpRequest(),
          url = options.url,
          type = options.type,
          async = options.async || true,
          // blob or arraybuffer. Default is blob
          dataType = options.responseType || "blob",
          data = options.data || null,
          username = options.username || null,
          password = options.password || null;

          xhr.addEventListener('load', function () {
            var data = {};
            data[options.dataType] = xhr.response;
            // make callback and send data
            callback(xhr.status, xhr.statusText, data, xhr.getAllResponseHeaders());
          });

          xhr.open(type, url, async, username, password);

          // setup custom headers
          for (var i in headers) {
            xhr.setRequestHeader(i, headers[i]);
          }

          xhr.responseType = dataType;
          xhr.send(data);
        },
        abort: function () {
          jqXHR.abort();
        }
      };
    }
  });
}


const downloadStorage = () => {
  $("#download-storage").click(() => {

    const key = $("#download-key").val()
    const data = {key: key}
    ajaxConfig()

    return $.ajax({
      url: '/api/v1/download/',
      type: 'post',
      data: JSON.stringify(data),
      contentType: 'application/json',
      processData: false,
      dataType: 'binary',
      success: (data, textStatus, jqXHR) => {
        const type = jqXHR.getResponseHeader('content-type')
        downloadFile(data, type, "storage.zip")
        $("#download-status").text("Download completed.")
      },
      error: (err) => {
        console.log(err)
        $("#download-status").text("Invalid key. Please check key entered.")
      }
    })
  })
}


$(document).ready(() => {
  fileInput()
  fileUpload()
  downloadStorage()
})
