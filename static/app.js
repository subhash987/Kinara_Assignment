function loadStudents() {
    const currentPage = new URLSearchParams(window.location.search).get('page');
    const url = currentPage ? `/?page=${currentPage}` : '/';
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const studentsBody = document.getElementById('students-body');
            studentsBody.innerHTML = '';

            data.students.forEach(student => {
                const row = document.createElement('tr');

                const idCell = document.createElement('td');
                idCell.textContent = student.id;
                row.appendChild(idCell);

                const nameCell = document.createElement('td');
                nameCell.textContent = student.name;
                row.appendChild(nameCell);

                const totalMarksCell = document.createElement('td');
                totalMarksCell.textContent = student.total_marks;
                row.appendChild(totalMarksCell);

                const ageCell = document.createElement('td');
                ageCell.textContent = student.age;
                row.appendChild(ageCell);

                const gradeCell = document.createElement('td');
                gradeCell.textContent = student.grade;
                row.appendChild(gradeCell);

                studentsBody.appendChild(row);
            });

            const currentPageElement = document.getElementById('current-page');
            const totalPages = Math.ceil(data.total_count / data.page_size);
            const currentPageNumber = parseInt(data.page) || 1;

            currentPageElement.innerHTML = '';

            if (totalPages > 1) {
                for (let i = 1; i <= totalPages; i++) {
                    const pageButton = document.createElement('button');
                    pageButton.textContent = i;
                    pageButton.onclick = function () {
                        goToPage(i);
                    };
                    if (i === currentPageNumber) {
                        pageButton.classList.add('active');
                    }
                    currentPageElement.appendChild(pageButton);
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}




function prevPage() {
    const currentPage = parseInt(new URLSearchParams(window.location.search).get('page'));
    const prevPage = currentPage > 1 ? currentPage - 1 : 1;
    const url = `/?page=${prevPage}`;
    window.location.href = url;
}

function nextPage() {
    const currentPage = parseInt(new URLSearchParams(window.location.search).get('page'));
    const nextPage = isNaN(currentPage) ? 2 : currentPage + 1;
    const url = `/?page=${nextPage}`;
    window.location.href = url;
}

function filterStudents() {
    const name = document.getElementById('name').value;
    const totalMarks = document.getElementById('total-marks').value;

    const criteria = {
        name: name.trim(),
        total_marks: parseInt(totalMarks)
    };

    const url = new URL('/', window.location.href);
    url.searchParams.set('page', 1);
    url.searchParams.append('criteria', JSON.stringify(criteria));

    window.location.href = url.href;
}

document.addEventListener('DOMContentLoaded', () => {
    loadStudents();
});


