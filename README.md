# Estra
*A pipeline to help automate and inform cinematic astrophysical data visualization using machine learning clustering algorithms.*

A proof of concept visualization of the Moon-forming synestia SPH simulation from [Lock et al. (2018)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017JE005333).

*Author:* 
[Patrick D. Aleo](https://astro.illinois.edu/directory/profile/paleo2)

## Description:

Scientific visualization tools are currently not optimized to create cinematic, production-quality representations of numerical data for science communication. In our pipeline Estra, we outline a step-by-step process from a raw simulation into a finished render as a way to teach non-experts in the field of visualization how to achieve production-quality outputs on their own. We demonstrate feasibility of using the visual effects software [Houdini](https://www.sidefx.com/products/houdini/) for cinematic astrophysical data visualization, informed by machine learning clustering algorithms. To demonstrate the capabilities of this pipeline, we used a post-impact, thermally-equilibrated Moon-forming synestia from [Lock et al. (2018)](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017JE005333). Our approach aims to identify "physically interpretable" clusters, where clusters identified in a temperature-entropy phase-space correspond to physically meaningful structures within the simulation data. Clustering results can then be used to highlight these structures (i.e. lower mantle, transition region, supercritical fluid region, isentropic pure-vapor region, and an outer vapor-dome region) by informing the color-mapping process in a simplified Houdini software shading network, where dissimilar phase-space clusters are mapped to different color values for easier visual identification. Cluster information can also be used in 3D position space, via Houdini's scene view, to aid inphysical cluster finding, simulation prototyping, and data exploration. Our clustering-based renders are compared to those created by the Advanced Visualization Lab (AVL) team for the full dome show "Imagine the Moon" as proof of concept.


## Visualizations:

Original synestia SPH dataset in Houdini scene view. 
<img src="https://github.com/patrickaleo/estra/blob/master/Notebooks/viewport_screenshots/standard_view_viewport.png" alt="syn_scene" width="512"/>

Example of the Estra visualization of the synestia, using a color mapping informed by a Gaussian Mixture Model (GMM) clustering algorithm and a simple, custom shading network detailed in [Estra](https://github.com/patrickaleo/estra/blob/master/Notebooks/Estra_v2.0.ipynb) and [Results to Render](https://github.com/patrickaleo/estra/blob/master/Notebooks/From_Results_to_Render.ipynb) notebooks.   
<img src="https://github.com/patrickaleo/estra/blob/master/Notebooks/final_renders/Estra_GMM_5clus.jpg" alt="Estra_render" width="512"/>

Example of the Advanced Visualization Lab (AVL) render of the synestia, created by a team of viz artists.
<img src="https://github.com/patrickaleo/estra/blob/master/Notebooks/final_renders/AVL_final.jpg" alt="AVL_render" width="512"/>

These two renders maintain the same view and scale as the viewport scene.

## Other Use Cases:

Estra in its current form can be applied to any SPH astronomical dataset, where the data is of emissive gas or dusty material, so the assumptions embedded in the shader hold true. Here is Estra applied to an example [Gadget](https://girder.hub.yt/#item/577c2a7f0d7c6b0001ad7867) disk galaxy, made of gas and dark matter. No clustering results have been run here, but the same Estra shader applied to the Synestia is used here, with the exception of using a different colormap based on internal energy, and not temperature directly (though internal energy is a proxy for temperature).

<img src="https://github.com/patrickaleo/estra/blob/master/gadget_disk_scene_view.png" alt="gadget_disk_scene_view" width="512"/>
<img src="https://github.com/patrickaleo/estra/blob/master/gadget_disk_4k_threshold75.jpg" alt="gadget_disk" width="512"/>
 

## Cite

```
@article{Aleo2020,
  title={Clustering-informed Cinematic Astrophysical Data Visualization ofthe Moon-forming Terrestrial Synestia},
  author={{Aleo}, P.~D. and others},
  year={2020},
  journal={MNRAS},
}
```

Please contact the author for any questions, at paleo2@illinois.edu.
