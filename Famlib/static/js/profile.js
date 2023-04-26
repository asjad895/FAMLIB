

// function uploadProfilePic() {
//     const input = document.getElementById('profile-pic-input');
//     const url = input.dataset.url;
//     const file = input.files[0];
    
//     const formData = new FormData();
//     formData.append('profile_pic', file);
    
//     const xhr = new XMLHttpRequest();
//     xhr.open('POST', url, true);
//     xhr.onload = function() {
//       if (xhr.status === 200) {
//         console.log('Image uploaded successfully');
//       } else {
//         console.error('Error uploading image');
//       }
//     };
//     xhr.send(formData);
// }

// const profilePic = document.querySelector('.profile_pic');
// profilePic.addEventListener('click', function() {
// const input = document.getElementById('profile-pic-input');
// input.click();
// });
    

function previewProfileImage() {
    var preview = document.querySelector('#profile-pic-preview');
    var file = document.querySelector('#profile-pic').files[0];
    var reader = new FileReader();

    reader.onloadend = function() {
        preview.src = reader.result;
        var cropper = new Cropper(preview, {
            aspectRatio: 1,
            crop: function(event) {
                var croppedImageDataURL = cropper.getCroppedCanvas({ width: 70, height: 70 }).toDataURL();
                preview.src = croppedImageDataURL;

                // Send the cropped image to the server using AJAX
                var formData = new FormData();
                formData.append('profile_pic', dataURItoBlob(croppedImageDataURL));
                $.ajax({
                    url: $('#profile-pic-input').data('url'),
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    success: function(data) {
                        console.log(data);
                    },
                    error: function(xhr, status, error) {
                        console.log(error);
                    }
                });
            }
        });
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "{% static 'img/default.png' %}";
    }
}

// Helper function to convert a data URI to a Blob object
function dataURItoBlob(dataURI) {
    var byteString = atob(dataURI.split(',')[1]);
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], { type: 'image/png' });
}
