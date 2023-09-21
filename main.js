
//Ensure only one menu open at a time
const collapseClasses = document.getElementById('collapseClasses');
const collapseProjects = document.getElementById('collapseProjects');

collapseClasses.addEventListener('show.bs.collapse', () => {
    if (collapseProjects.classList.contains('show')) {
        collapseProjects.classList.remove('show');
    }
});

collapseProjects.addEventListener('show.bs.collapse', () => {
    if (collapseClasses.classList.contains('show')) {
        collapseClasses.classList.remove('show');
    }
});
        

