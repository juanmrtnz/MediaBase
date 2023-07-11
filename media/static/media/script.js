function changeToTextarea() {
    const title = document.querySelector('#form-title');
    const textarea = document.querySelector('#form-textarea');
    const textarea_hidden = document.querySelector('#form-textarea-hidden');
    const buttonOff_title = document.querySelector('#form-toggleButtonOff');
    const buttonOn_textarea = document.querySelector('#form-toggleButtonOn');
    const toggleIconDown = document.querySelector('#form-toggleIconDown');
    const toggleIconUp = document.querySelector('#form-toggleIconUp');

    buttonOn_textarea.disabled = false;
    buttonOff_title.disabled = true;

    toggleIconDown.style.animationPlayState = 'running';

    title.style.animationPlayState = 'running';
    title.addEventListener('animationend', () => {
        title.style.animationPlayState = 'paused';
        title.style.display = 'none';
        document.querySelector('#form-title-title').innerHTML = 'Multiple titles';
        title.required = false;
        title.value = "";

        const text = textarea.value;
        textarea_hidden.value = text;
        
        textarea_hidden.style.display = 'block';
        textarea_hidden.style.animationPlayState = 'running';
        textarea_hidden.addEventListener('animationend', () => {
            textarea_hidden.style.animationPlayState = 'paused';
            textarea_hidden.style.display = 'none';
            textarea.style.display = 'block';
            textarea.required = true;
            textarea.focus();
            buttonOff_title.style.display = 'none';
            buttonOn_textarea.style.display = 'block';
            toggleIconDown.style.animationPlayState = 'paused';
            toggleIconDown.style.display = 'none';
            toggleIconUp.style.display = 'block';
        });
    });
}

function changeToTitle() {
    const title = document.querySelector('#form-title');
    const title_hidden = document.querySelector('#form-title-hidden');
    const textarea = document.querySelector('#form-textarea');
    const buttonOff_title = document.querySelector('#form-toggleButtonOff');
    const buttonOn_textarea = document.querySelector('#form-toggleButtonOn');
    const toggleIconDown = document.querySelector('#form-toggleIconDown');
    const toggleIconUp = document.querySelector('#form-toggleIconUp');

    buttonOff_title.disabled = false;
    buttonOn_textarea.disabled = true;

    toggleIconUp.style.animationPlayState = 'running';

    textarea.style.animationPlayState = 'running';
    textarea.addEventListener('animationend', () => {
        textarea.style.animationPlayState = 'paused';
        textarea.style.display = 'none';
        document.querySelector('#form-title-title').innerHTML = 'Title';
        textarea.required = false;

        title_hidden.style.display = 'block';
        title_hidden.style.animationPlayState = 'running';
        title_hidden.addEventListener('animationend', () => {
            title_hidden.style.animationPlayState = 'paused';
            title_hidden.style.display = 'none';
            title.style.display = 'block';
            title.required = true;
            title.focus();
            buttonOff_title.style.display = 'block';
            buttonOn_textarea.style.display = 'none';
            toggleIconUp.style.animationPlayState = 'paused';
            toggleIconUp.style.display = 'none';
            toggleIconDown.style.display = 'block';
        });
    });
}

function editRow(rowId) {

    stopEditing();

    document.querySelector('#form-submitButton').value = 'Edit item';

    document.querySelector('#form-stopEditingButton').style.display = 'inline';
    
    const row = document.querySelector(`#table-${rowId}-row`);
    row.style.backgroundColor = 'white';
    const form = document.querySelector('#form');
    form.action = form.action.split('/').slice(0, -1).join('/') + '/' + rowId;

    const form_title = document.querySelector('#form-title');
    const title_hidden = document.querySelector('#form-title-hidden');
    const textarea = document.querySelector('#form-textarea');
    const toggleIconUp = document.querySelector('#form-toggleIconUp');
    const buttons_icons_textarea = document.querySelectorAll('.form-toggleIcon, .form-toggleButton, #form-textarea');

    if (textarea.style.display === 'block') {
        toggleIconUp.style.animationPlayState = 'running';
        textarea.style.animationPlayState = 'running';
        textarea.addEventListener('animationend', () => {
            textarea.style.animationPlayState = 'paused';
            textarea.style.display = 'none';
            document.querySelector('#form-title-title').innerHTML = 'Title';
            textarea.required = false;
    
            title_hidden.style.display = 'block';
            title_hidden.style.animationPlayState = 'running';
            title_hidden.addEventListener('animationend', () => {
                title_hidden.style.animationPlayState = 'paused';
                title_hidden.style.display = 'none';
                form_title.style.display = 'block';
                form_title.required = true;
                toggleIconUp.style.animationPlayState = 'running';
                
                buttons_icons_textarea.forEach(element => {
                    element.style.display = 'none';
                })
                form.style.backgroundColor = 'rgb(240,240,240)';
            })  
        })
    } else {
        buttons_icons_textarea.forEach(element => {
            element.style.display = 'none';
        })
        form.style.backgroundColor = 'rgb(240,240,240)';
    }

    const title = document.querySelector(`#item-${rowId}-title`).innerHTML.trim().replaceAll('&amp;', '&');
    let releaseDate = document.querySelector(`#item-${rowId}-releaseDate`);
    let genre = document.querySelector(`#item-${rowId}-genre`);
    let genres = document.querySelector(`#item-${rowId}-genres`);
    const subgenre = document.querySelector(`#item-${rowId}-subgenre`);
    const platform = document.querySelector(`#item-${rowId}-platform`);
    const series = document.querySelector(`#item-${rowId}-series`);
    const author = document.querySelector(`#item-${rowId}-author`);
    const language = document.querySelector(`#item-${rowId}-language`);
    const finishedDate = document.querySelector(`#item-${rowId}-finishedDate`);
    const notes = document.querySelector(`#item-${rowId}-notes`).innerHTML.trim().replaceAll('&amp;', '&');

    const form_releaseDate = document.querySelector('#form-releaseDate');
    const form_releaseYear = document.querySelector('#form-releaseYear');
    const form_genre = document.querySelector('#form-genre');
    const form_genre_2 = document.querySelector('#form-genre2');
    const form_subgenre = document.querySelector('#form-subgenre');
    const form_series = document.querySelector('#form-series');
    const form_author = document.querySelector('#form-author');
    const form_status_finished =  document.querySelector('#form-status-finished');
    const form_status_planToFinish =  document.querySelector('#form-status-planToFinish');
    const form_status_ongoing =  document.querySelector('#form-status-ongoing');
    const form_status_dropped =  document.querySelector('#form-status-dropped');
    const form_status_noStatus =  document.querySelector('#form-status-noStatus');
    const form_notes = document.querySelector('#form-notes');

    form_title.value = title;
    if (row.className === "table-row-planToFinish") {
        form_status_finished.checked = false;
        form_status_planToFinish.checked = true;
    }
    if (row.className === "table-row-dropped") {
        form_status_finished.checked = false;
        form_status_dropped.checked = true;
    }
    if (row.className === "table-row-ongoing") {
        form_status_finished.checked = false;
        form_status_ongoing.checked = true;
    }
    if (row.className === "table-row-noStatus") {
        form_status_finished.checked = false;
        form_status_noStatus.checked = true;
    }
    if (releaseDate !== null) {
        releaseDate = releaseDate.innerHTML.trim();
        if (releaseDate.length > 4) {
            const date_array = releaseDate.split('/');
            let day = date_array[0];
            if (day.length == 1) {
                day = `0${day}`;
            }
            let month = date_array[1];
            if (month.length == 1) {
                month = `0${month}`;
            }
            let year = date_array[2];
            const final_releaseDate = `${year}-${month}-${day}`

            form_releaseDate.value = final_releaseDate;
        } else {
            form_releaseYear.value = releaseDate;
        }
    }
    if (genre === null && genres !== null) {
        genres = genres.innerHTML.trim().split(', ');
        genre = genres[0];
        const genre_2 = genres[1];
        form_genre.value = genre;
        form_genre_2.value = genre_2;
    } else if (genre !== null) {
        if (form_genre_2 !== null) {
            form_genre_2.value = "";
        }
        form_genre.value = genre.innerHTML.trim();
    }
    if (subgenre !== null) {
        form_subgenre.value = subgenre.innerHTML.trim();
    }

    editArrayFieldCell(platform, 'platform')

    if (series !== null) {
        form_series.value = series.innerHTML.trim().replaceAll('&amp;', '&');
    }
    if (author !== null) {
        form_author.value = author.innerHTML.trim().replaceAll('&amp;', '&');
    }

    editArrayFieldCell(language, 'language')

    editArrayFieldCell(finishedDate, 'finishedDate')

    form_notes.value = notes;

    window.scrollTo({top: 0, behavior: 'smooth'});
}

function stopEditing() {
    const form = document.querySelector('#form');
    media = form.action.split('/').slice(-2);
    media = media[0];
    form.action = `post/${media}/new`;

    document.querySelector('#form-toggleIconDown').style.display = 'block';
    document.querySelector('#form-toggleButtonOff').style.display = 'block';

    document.querySelectorAll('.form-input').forEach(input => {
        input.value = "";
    });

    document.querySelector('#form-status-finished').checked = true;

    if (document.querySelector('#form-platform') !== null) {
        document.querySelector('#form-platform').style.height = '20px';
    }

    if (document.querySelector('#form-language') !== null) {
        document.querySelector('#form-language').style.height = '20px';
    }

    document.querySelector('#form-finishedDate').style.height = '20px';

    document.querySelector('#form-stopEditingButton').style.display = 'none';

    document.querySelector('#form-submitButton').value = 'Add item';

    document.querySelector('#form').style.backgroundColor = 'white';

    document.querySelectorAll('.table-title, .table-notes').forEach(element => {
        element.style.whiteSpace = 'nowrap';
    });

    document.querySelectorAll('.table-row-finished').forEach(row => {
        row.style.backgroundColor = 'rgb(220, 255, 220)';
    });
    document.querySelectorAll('.table-row-planToFinish').forEach(row => {
        row.style.backgroundColor = 'rgb(255, 243, 220)';
    });
    document.querySelectorAll('.table-row-ongoing').forEach(row => {
        row.style.backgroundColor = 'rgb(220, 243, 255)';
    });
    document.querySelectorAll('.table-row-dropped').forEach(row => {
        row.style.backgroundColor = 'rgb(255, 220, 220)';
    });
}

function openRow(rowId) {
    const row = document.querySelector(`#table-${rowId}-row`);
    const cells = row.children;
    for (let i=0; i < cells.length; i++) {
        cells[i].style.whiteSpace = "normal";
    }

    const closeRow = function() {
        row.removeEventListener('click', closeRow);

        for (let i=0; i < cells.length; i++) {
            cells[i].style.whiteSpace = "nowrap";
        }
    }

    row.addEventListener('click', closeRow);
}

function deleteRow(rowId) {
    const form = document.querySelector('#form');
    media = form.action.split('/').slice(-2);
    media = media[0];

    const warning = document.querySelector('#deleteWarning-container');
    const title = document.querySelector(`#item-${rowId}-title`).innerHTML.trim();
    const deleteMessage_div = document.querySelector('#deleteWarning-message');

    deleteMessage_div.innerHTML = `Are you sure you want to delete the ${media}<br>"<b>${title}</b>"?`;
    
    document.querySelector('#deleteWarning-container').style.display = 'flex';

    const yes_button = document.querySelector('#deleteWarning-yesButton');
    const no_button = document.querySelector('#deleteWarning-noButton');

    const deleteFunc = function () {
        yes_button.removeEventListener('click', deleteFunc);
        no_button.removeEventListener('click', cancelFunc);

        warning.style.display = 'none';

        fetch(`/delete/${media}/${rowId}`, {
            method: 'POST',
            headers: {"X-CSRFToken": csrftoken}
        })
        document.querySelector(`#table-${rowId}-buttons`).innerHTML = '';
        const row = document.querySelector(`#table-${rowId}-row`);
        const cells = row.children;
        for (let i=0; i < cells.length; i++) {
            cells[i].style.animationPlayState = "running";
        }
        setTimeout(() => {
            row.remove();
        }, 950);

        stopEditing();
    }

    const cancelFunc = function () {
        yes_button.removeEventListener('click', deleteFunc);
        no_button.removeEventListener('click', cancelFunc);

        warning.style.display = 'none';
    }

    yes_button.addEventListener('click', deleteFunc);
    no_button.addEventListener('click', cancelFunc);
}

function editArrayFieldCell(cell, form_input) {
    if (cell !== null && cell.innerHTML !== "") {
        let cell_list = cell.innerHTML.replaceAll('\r\n', '');
        cell_list = cell_list.split(', ');
        let string = '';
        let elements = 0;
        for (i=0; i < cell_list.length; i++) {
            if (i === cell_list.length - 1) {
                string = string + cell_list[i].trim();
            } else {
                string = string + cell_list[i].trim() + '\r\n';
            }
            elements ++;
        }
        const form_cell = document.querySelector(`#form-${form_input}`)
        if (elements === 2) {
            form_cell.style.height = '40px';
        }
        else if (elements > 2) {
            form_cell.style.height = '58px';
        }
        form_cell.value = string.replaceAll('&amp;', '&');
    }

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i=0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
