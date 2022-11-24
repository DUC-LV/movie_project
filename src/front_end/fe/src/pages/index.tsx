import React, { useEffect, useState } from "react";
import { Box } from "theme-ui";
import Slide from "../components/Slide";
import SlideLiveStream from "../components/SlideLiveStream";
import SlideLiveVideo from "../components/SlideLiveVideo";
import SlideShow from "../components/SlideShow";
import getBanner from "../service/getBanner";
import getLiveFilm from "../service/getLiveFilm";
import getLiveStream from "../service/getLiveStream";
import getLiveTV from "../service/getLiveTV";
import getLiveVideo from "../service/getLiveVideo";
interface DataBanner {
	image: string | undefined;
	name: string | undefined;
	id: number | undefined;
}
const Home = () => {
	const [dataBanner, setDataBanner] = useState<Array<DataBanner>>([]);
	const [dataLiveTV, setDataLiveTV] = useState<Array<DataBanner>>([]);
	const [dataLiveStream, setDataLiveStream] = useState<Array<DataBanner>>([]);
	const [dataLiveVideo, setDataLiveVideo] = useState<Array<DataBanner>>([]);
	const [dataLiveFim, setDataLiveFilm] = useState<Array<DataBanner>>([]);
	const [title, setTitle] = useState('');
	const [titleLiveStream, setTitleLiveStream] = useState('');
	const [titleLiveVideo, setTitleLiveVideo] = useState('');
	const [titleLiveFilm, setTitleLiveFilm] = useState('');
	useEffect(() => {
		getBanner.getAll().then(res => {
			setDataBanner(res.data.data);
		})
		getLiveTV.getAll().then(res => {
			setTitle(res.data.name);
			setDataLiveTV(res.data.data);
		})
		getLiveStream.getAll().then(res => {
			console.log(res.data)
			setTitleLiveStream(res.data.name);
			setDataLiveStream(res.data.data);
		})
		getLiveVideo.getAll().then(res => {
			setDataLiveVideo(res.data.data);
			setTitleLiveVideo(res.data.name);
		})
		getLiveFilm.getAll().then(res => {
			setDataLiveFilm(res.data.data);
			setTitleLiveFilm(res.data.name);
		})
		.catch(err => {
			console.log(err.message);
		})
	}, [])
	return(
		<Box>
			<Slide 
				dataSlide={dataBanner?.map((item:any) => {
					return {
						image:item?.urlImage,
						message: item?.message,
						title: item?.title,
						id: item?._id,
					}
				})}
			/>
			<SlideShow
				dataSlide={dataLiveTV?.map((item:any) => {
					return {
						image: item?.coverImage,
						name: item?.name,
						id: item?._id,
					}
				})}
				name={title}
			/>
			<SlideLiveStream
				dataSlide={dataLiveStream?.map((item:any) => {
					return {
						image: item?.urlImage,
						name: item?.name,
						id: item?._id,
					}
				})}
				name={titleLiveStream}
			/>
			<SlideLiveVideo
				dataSlide={dataLiveVideo?.map((item:any) => {
					return {
						image: item?.coverImage,
						name: item?.name,
						id: item?._id,
					}
				})}
				name={titleLiveVideo}
			/>
			<SlideShow
				dataSlide={dataLiveFim?.map((item:any) => {
					return {
						image: item?.coverImageH,
						name: item?.name,
						id: item?._id,
					}
				})}
				name={titleLiveFilm}
			/>
		</Box>
	);
}
export default Home;