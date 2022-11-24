import axiosInstance from "./axiosInstance ";

const getLiveFilm = {
    getAll(){
        const url = '/live-film'
        return axiosInstance.get(url)
    }
}
export default getLiveFilm;