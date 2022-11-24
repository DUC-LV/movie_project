import axiosInstance from "./axiosInstance ";

const getBanner = {
    getAll(){
        const url = '/banner'
        return axiosInstance.get(url)
    }
}
export default getBanner;