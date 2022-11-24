import React from "react";
import { Box, Text, Image, Flex } from "theme-ui";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from "react-slick";
export interface ResponsiveObject {
    breakpoint:number,
    slidesToShow:number,
    slidesToScroll: number
}
export interface ReposiveSlide {
    reposiveSlide: ResponsiveObject[]
}
export interface DataSlider {
	image: string | undefined;
	name: string | undefined;
	id: number | undefined;
}
export interface DataSlide {
	dataSlide: DataSlider[];
	name: string;
}
const SlideShow = ({ dataSlide, name }: DataSlide) => {
	const setting = {
		infinite: true,
		slidesToShow: 5,
		slidesToScroll: 5,
	}
	const responsiveSettings = [
		{
			breakpoint: 500,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 3,
			}
		},
		{
			breakpoint: 768,
			settings: {
				slidesToShow: 5,
				slidesToScroll: 5,
			}
		},
		{
			breakpoint: 1123,
			settings: {
				slidesToShow: 5,
				slidesToScroll: 5,
			}
		},
	];
	// const router = useRouter();
	return(
		<Box
			sx={{
				"@media only screen and (max-width: 768px)": {
					margin: "50px 10px 0px 20px",
				},
				"@media only screen and (min-width: 768px) and (max-width: 1023px)": {
					margin: "50px 40px 0px 40px",
				},
				"@media only screen and (min-width: 1024px) and (max-width: 1123px)": {
					margin: "50px 100px 0px 100px",
				},
				"@media only screen and (min-width: 1124px)": {
					margin: "50px 200px 0px 200px",
				}
			}}
		>
			<Text 
				as="h2"
				sx={{
					color: "rgba(255,255,255,0.87)",
				}}
			>{name}</Text>
			<Slider {...setting} responsive={responsiveSettings}>
				{dataSlide?.map((item:any, index: any) => {
					return(
						<Box 
							key={index}
							sx={{
								mt: '20px',
								outline: 'none',
							}}
						>
							<Image
								// onClick={() => {
								// 	router.push({
								// 		pathname: "/movie/[slugMovie]",
								// 		query: { 
								// 			slugMovie: convertSlug(item?.name),
								// 			id: item?.id
								// 		}
								// 	})
								// }}
								sx={{
									borderRadius: "10px",
									width: '95%',
									"@media only screen and (min-width: 768px) and (max-width: 1023px)": {
										height: '200px'
									},
									"@media only screen and (min-width: 1124px)": {
										cursor: "pointer",
										":hover": {
											border: "3px solid red",
										},
									},
									"@media only screen and (max-width: 768px)": {
										height: '200px',
									},
								}}
								alt=""
								src={item.image} 
							/>
						</Box>
					)
				})}
			</Slider>
		</Box>
	)
}
export default SlideShow;