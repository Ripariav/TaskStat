document.addEventListener('DOMContentLoaded', function() {
  var editBtn = document.getElementById('edit-btn');
  var cancelBtn = document.getElementById('cancel-btn');
  var profileInfo = document.getElementById('profile-info');
  var profileForm = document.getElementById('profile-form');

  editBtn.addEventListener('click', function() {
    profileInfo.classList.add('hidden');  // Ocultar información del perfil
    profileForm.classList.remove('hidden');  // Mostrar formulario de edición
  });

  cancelBtn.addEventListener('click', function() {
    profileForm.classList.add('hidden');  // Ocultar formulario de edición
    profileInfo.classList.remove('hidden');  // Mostrar información del perfil
  });
});