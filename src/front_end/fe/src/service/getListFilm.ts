import axiosInstance from "./axiosInstance ";

const getListFilm = {
    getAll(){
        const url = '/list-film'
        return axiosInstance.get(url)
    }
}
export default getListFilm;