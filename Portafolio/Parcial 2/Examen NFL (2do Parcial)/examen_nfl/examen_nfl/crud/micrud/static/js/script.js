(function(){

    const btnEliminacion=document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
            const confirmacion=confirm('Are you sure about deleting this team?');
            if(!confirmacion){
                e.preventDefault();
            }
        })
    })

    
})();