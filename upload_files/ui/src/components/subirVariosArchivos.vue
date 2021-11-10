<template>
  <div>
    <h3>Subir varios - con 1 solo campo de input</h3>
    <input type="file" @change="onFileSelected" multiple="multiple" />
    <button @click="onUpload">Upload</button>
  </div>
</template>

<script>
// yarn add axios
import axios from 'axios';

export default {
  data() {
    return {
      selectedFiles: null,
    };
  },
  methods: {
    onFileSelected(event) {
      this.selectedFiles = event.target.files;
    },
    onUpload(){
      if (!this.selectedFiles) {
        alert("Por favor elija un archivo")
        return
      }

      const fd = new FormData();
      let file;

      for (let i = 0; i < this.selectedFiles.length; i++) {
          file = this.selectedFiles.item(i);
          fd.append('files', file)
      }
      
      axios.post("http://127.0.0.1:8000/upload/files", fd, {
        onUploadProgress: uploadEvent => {
          console.log(`Upload progress: ${Math.round(uploadEvent.loaded / uploadEvent.total * 100)} %`)
        }
      })
        .then(res => {
          console.log(res)
        })
        .catch(res => {
          alert("Hubo un error en la carga de los archivos")
        })
    }
  },
}
</script>

<style>
</style>