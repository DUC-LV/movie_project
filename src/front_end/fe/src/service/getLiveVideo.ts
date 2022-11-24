import axiosInstance from "./axiosInstance ";

const getLiveVideo = {
    getAll(){
        const url = '/live-video';
        return axiosInstance.get(url);
    }
}
export default getLiveVideo;