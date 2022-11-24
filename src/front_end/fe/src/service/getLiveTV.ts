import axiosInstance from "./axiosInstance ";

const getLiveTV = {
    getAll(){
        const url = '/live-tv'
        return axiosInstance.get(url)
    }
}
export default getLiveTV;