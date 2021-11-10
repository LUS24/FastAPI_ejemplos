<template>
  <div>
    <h3>Subir de a 1 archivo</h3>
    <input type="file" @change="onFileSelected" />
    <button @click="onUpload">Upload</button>
  </div>
</template>

<script>
// yarn add axios
import axios from 'axios';

export default {
  data() {
    return {
      selectedFile: null,
    };
  },
  methods: {
    onFileSelected(event) {
      this.selectedFile = event.target.files[0];
    },
    onUpload(){
      if (!this.selectedFile) {
        alert("Por favor elija un archivo")
        return
      }

      const fd = new FormData();
      fd.append('file', this.selectedFile)
      axios.post("http://127.0.0.1:8000/upload/file", fd, {
        onUploadProgress: uploadEvent => {
          console.log(`Upload progress: ${Math.round(uploadEvent.loaded / uploadEvent.total * 100)} %`)
        }
      })
        .then(res => {
          console.log(res)
        })
    }
  },
}
</script>

<style>
</style>