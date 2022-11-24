import axiosInstance from "./axiosInstance ";

const getLiveStream = {
    getAll(){
        const url = '/live-streaming'
        return axiosInstance.get(url)
    }
}
export default getLiveStream;