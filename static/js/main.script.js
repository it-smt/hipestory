// Меню бургер.

const menuIcon = document.querySelector('#menuIcon');
const menuBody = document.querySelector('#menuBody');

menuIcon.addEventListener('click', () => {
    menuIcon.classList.toggle('_active');
    menuBody.classList.toggle('_active');
    document.body.classList.toggle('_lock');
});

// End Меню бургер.

function isMobile() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

// Изображение профиля.

const profileImage = document.querySelector('#profileImage');
const profileImageMenu = document.querySelector('#profileImageMenu');

if (profileImage) {
    if (isMobile()) {
        profileImage.addEventListener('click', () => {
            profileImageMenu.classList.toggle('_active');
        });
    } else {
        profileImage.onmouseover = () => {
            profileImageMenu.classList.add('_active');
        }
        profileImage.onmouseout = () => {
            profileImageMenu.classList.remove('_active');
        }
    }
}

// End Изображение профиля.

// Cropper

const cutImage = document.getElementById('cutImage');

if (cutImage) {
    const cropper = new Cropper(cutImage, {
        aspectRatio: 1,
        viewsMode: 0,
        dragMode: 'move',
        autoCropArea: 1,
        cropBoxResizable: true,
        cropBoxMovable: true,
        toggleDragModeOnDblclick: false,
        zoomable: true,
        guides: false,
        background: false,
    });

    const cropButton = document.getElementById('cropButton');

    if (cropButton) {
        let hiddenInput = document.getElementById('id_hidden');
        const form = document.getElementById('form');
        cropButton.addEventListener('click', () => {
            let croppedImage = cropper.getCroppedCanvas().toDataURL('image/png');
            hiddenInput.value = croppedImage;
            form.submit();
        });
    }
}

// End Cropper

// Change Avatar

document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('#id_avatar');
    const label = document.querySelector('#inputFileLabel')
    let labelVal;
    if (label) {
        labelVal = label.innerHTML;
    }
    if (input) {
        input.addEventListener('change', () => {
            console.log(input.files);
            let fileName = '';
            if (input.files && input.files.length > 1) {
                fileName = (input.getAttribute('data-multiple-caption') || '').replace('{count}', input.files.length);
            } else {
                fileName = input.files[0].name;
            }

            if (fileName) {
                label.querySelector('span').innerHTML = fileName;
            } else {
                label.innerHTML = labelVal;
            }
        });
    }
});

// End Change Avatar