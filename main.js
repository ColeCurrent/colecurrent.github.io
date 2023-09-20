<!-- Ensure only one button is open at a time -->
    <script>
        const collapseClasses = document.getElementById('collapseClasses');
        const collapseProjects = document.getElementById('collapseProjects');

        // Add event listeners to handle collapsible show and hide events
        collapseClasses.addEventListener('show.bs.collapse', () => {
            // Close the other collapsible (if open)
            if (collapseProjects.classList.contains('show')) {
                collapseProjects.classList.remove('show');
            }
        });

        collapseProjects.addEventListener('show.bs.collapse', () => {
            // Close the other collapsible (if open)
            if (collapseClasses.classList.contains('show')) {
                collapseClasses.classList.remove('show');
            }
        });
        
    </script>
